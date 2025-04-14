from django.test import TestCase
from django.urls import reverse

from apps.shortener.models import ShortUrl
from apps.shortener.utils import Encoder


class UrlShortenerTests(TestCase):
    def test_create_short_url_successfully(self):
        payload = {"url": "https://www.django-rest-framework.org/api-guide/serializers/#modelserializer"}
        response = self.client.post(reverse("shortly"), data=payload)
        self.assertEqual(response.status_code, 201)

        slug = Encoder.retrive_key(payload["url"])
        self.assertTrue(ShortUrl.objects.filter(slug=slug, url=payload["url"]).exists())
