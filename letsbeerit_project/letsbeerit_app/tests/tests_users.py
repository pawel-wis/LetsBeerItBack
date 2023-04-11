from rest_framework.test import APITestCase
from django.test import TestCase
from ..models import AppUser
from rest_framework.authtoken.models import Token
from ..models import SocialGroup


class TestUsersListView(TestCase):
    def test_users_list_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 401)


class TestGetTokenView(APITestCase):
    def setUp(self) -> None:
        self.token_initial_count = Token.objects.count()
        self.group = SocialGroup.objects.create(name="test")
        self.group.save()
        self.user_cred = {"username": "test", "password": "test123"}
        self.user = AppUser.objects.create_user(
            username=self.user_cred['username'],
            password=self.user_cred['password'],
            group_id=self.group
        )
        self.user.save()

    def tearDown(self) -> None:
        self.user.delete()
        self.group.delete()

    def test_token_generation_after_user_create(self):
        self.assertGreater(Token.objects.count(), self.token_initial_count)

    def test_user_get_token_after_credential(self):
        response = self.client.post(path='/users/get-token/', data={"username": self.user_cred['username'],
                                                                    "password": self.user_cred['password']},
                                    format='json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'token')

    def test_user_group_alignment(self):
        self.assertIsNotNone(self.user.group_id)
