from factory.django import DjangoModelFactory
from ...models import AppUser, SocialGroup
from factory.faker import Faker


class AppUserFactory(DjangoModelFactory):
    class Meta:
        model = AppUser

    username = Faker("user_name")
    password = Faker("password")


class SoliacGroupFactory(DjangoModelFactory):
    class Meta:
        model = SocialGroup

    name = Faker("sentence", nb_words=3)