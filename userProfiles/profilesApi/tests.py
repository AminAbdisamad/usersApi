from django.test import TestCase

# Create your tests here.
class APITests(TestCase):
    def test_api_home_status_code(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)

