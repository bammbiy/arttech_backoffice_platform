from django.urls import reverse
from rest_framework.test import APITestCase


class SwaggerTest(APITestCase):

    def test_swagger_schema(self):
        url = reverse("schema")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)