from django.test import TestCase
from django.urls import reverse


class UrlsTest(TestCase):
    def test_index_url(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_lettings_namespace_url(self):
        response = self.client.get(reverse("lettings:index"))
        self.assertEqual(response.status_code, 200)

    def test_profiles_namespace_url(self):
        response = self.client.get(reverse("profiles:index"))
        self.assertEqual(response.status_code, 200)

    def test_custom_404_handler(self):
        response = self.client.get("/nonexistent-page/")
        self.assertEqual(response.status_code, 404)
