import factory
from factory.django import DjangoModelFactory
from ...models import AppUser, SocialGroup, SocialMembership, UserPin
from factory.faker import Faker


class UserPinFactory(DjangoModelFactory):
    class Meta:
        model = UserPin

    alt_name = Faker("sentence", nb_words=3)
    latitude = Faker("latitude")
    longitude = Faker("longitude")


class AppUserFactory(DjangoModelFactory):
    class Meta:
        model = AppUser

    username = Faker("user_name")
    password = Faker("password")
    email = Faker("email")
    user_pin = factory.SubFactory(UserPinFactory)


class SocialGroupFactory(DjangoModelFactory):
    class Meta:
        model = SocialGroup

    name = Faker("sentence", nb_words=3)
    description = Faker("sentence", nb_words=10)


class SocialMembershipFactory(DjangoModelFactory):
    class Meta:
        model = SocialMembership

    appuser = factory.SubFactory(AppUserFactory)
    socialgroup = factory.SubFactory(SocialGroupFactory)
    role_user_in_group = Faker("random_element", elements=("member", "admin"))
