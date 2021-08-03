from django.http import response
from django.test import TestCase, SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_playground_hello(self):
        response = self.client.get('/playground/hello/')
        self.assertEqual(response.status_code, 200)

