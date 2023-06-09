from .test_utils import factories
from rest_framework.test import APITestCase
from django.db.utils import IntegrityError
from ..models import AppUser, SocialGroup, SocialMembership, UserPin


class UserPinTestCase(APITestCase):
    def test_create_pin(self):
        pins = factories.UserPinFactory.create_batch(10)
        mandatory_fields = ["alt_name", "latitude", "longitude"]
        for pin in pins:
            self.assertIsInstance(pin, UserPin)
            for field in mandatory_fields:
                self.assertTrue(hasattr(pin, field))
                self.assertIsNotNone(getattr(pin, field))


class AppUserTestCase(APITestCase):

    def test_create_user(self):
        users = factories.AppUserFactory.create_batch(10)
        mandatory_fields = ["username", "password", "email"]
        for user in users:
            self.assertIsInstance(user, AppUser)
            for field in mandatory_fields:
                self.assertTrue(hasattr(user, field))
                self.assertIsNotNone(getattr(user, field))

    def test_user_with_pin_location(self):
        user = factories.AppUserFactory.create()
        pin = factories.UserPinFactory.create()
        user.user_pin = pin
        user.save()
        self.assertEqual(user.user_pin, pin)
        saved_user = AppUser.objects.get(username=user.username)
        self.assertEqual(saved_user.user_pin, pin)

    def test_unique_user_name(self):
        user1 = factories.AppUserFactory.create(username="test_user")
        with self.assertRaises(IntegrityError):
            user2 = factories.AppUserFactory.create(username="test_user")


class SocialGroupTestCase(APITestCase):
    def test_create_group(self):
        groups = factories.SocialGroupFactory.create_batch(10)
        mandatory_fields = ["name", "description"]
        for group in groups:
            self.assertIsInstance(group, SocialGroup)
            for field in mandatory_fields:
                self.assertTrue(hasattr(group, field))
                self.assertIsNotNone(getattr(group, field))

    def test_unique_group_name(self):
        group1 = factories.SocialGroupFactory.create(name="test_group")
        with self.assertRaises(IntegrityError):
            group2 = factories.SocialGroupFactory.create(name="test_group")


class SocialMembershipTestCase(APITestCase):
    def setUp(self) -> None:
        self.memberships = factories.SocialMembershipFactory.create_batch(10)

    def test_create_membership(self):
        mandatory_fields = ["appuser", "socialgroup", "role_user_in_group"]
        for membership in self.memberships:
            self.assertIsInstance(membership, SocialMembership)
            for field in mandatory_fields:
                self.assertTrue(hasattr(membership, field))
                self.assertIsNotNone(getattr(membership, field))

    def test_unique_membership(self):
        with self.assertRaises(IntegrityError):
            membership2 = factories.SocialMembershipFactory.create(appuser=self.memberships[0].appuser,
                                                                   socialgroup=self.memberships[0].socialgroup)
