from django.test import TestCase, SimpleTestCase


class simpleTests(SimpleTestCase):
    def test_about_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
