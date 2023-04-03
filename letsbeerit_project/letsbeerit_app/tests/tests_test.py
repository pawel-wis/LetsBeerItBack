from django.test import TestCase


# Create your tests here.
class TestView(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello World')
