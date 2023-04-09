from django.test import TestCase


# Create your tests here.
class TestView(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello World')


class TestUsersListView(TestCase):
    def test_users_list_view(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 401)
        self.assertContains(response, 'Authentication credentials were not provided')

    def test_users_authentication(self):
        pass