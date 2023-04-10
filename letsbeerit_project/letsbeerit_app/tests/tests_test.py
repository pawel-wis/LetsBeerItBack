from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


# Create your tests here.
class TestView(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello World')


class TestUsersListView(TestCase):
    def test_users_list_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 401)


class TestGetTokenView(APITestCase):
    def setUp(self) -> None:
        self.token_initial_count = Token.objects.count()
        self.user = User.objects.create_user(
            username='test',
            password='test123'
        )
        self.user.save()

    def tearDown(self) -> None:
        self.user.delete()

    def test_token_generation_after_user_create(self):
        self.assertGreater(Token.objects.count(), self.token_initial_count)
