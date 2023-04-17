import factory
from factory.django import DjangoModelFactory
from ...models import AppUser, SocialGroup, SocialMembership
from factory.faker import Faker


class AppUserFactory(DjangoModelFactory):
    class Meta:
        model = AppUser

    username = Faker("user_name")
    password = Faker("password")
    email = Faker("email")


class SocialGroupFactory(DjangoModelFactory):
    class Meta:
        model = SocialGroup

    name = Faker("sentence", nb_words=3)
    description = Faker("sentence", nb_words=10)


class SocialMembershipFactory(DjangoModelFactory):
    class Meta:
        model = SocialMembership
        # django_get_or_create = ("appuser", "socialgroup")

    appuser = factory.SubFactory(AppUserFactory)
    socialgroup = factory.SubFactory(SocialGroupFactory)
    role_user_in_group = Faker("random_element", elements=("member", "admin"))
