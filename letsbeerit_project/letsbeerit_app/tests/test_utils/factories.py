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

    user = AppUserFactory()
    group = SocialGroupFactory()
    appuser_group_role = Faker("random_element", elements=("member", "admin"))

