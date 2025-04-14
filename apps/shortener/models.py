from urllib.parse import urljoin

from django.db import models


class ShortUrl(models.Model):
    slug = models.SlugField(max_length=8, primary_key=True, help_text="Key used for retrive a short url")
    url = models.URLField(max_length=256, help_text="The original URL was shorten")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, help_text="The date was created this url")
    updated_at = models.DateTimeField(auto_now=True, blank=True, help_text="The date was updated this url")

    @property
    def shorted(self) -> str:
        """
        The shortened url
        """
        from django.conf import settings

        return urljoin(settings.REDIRECT_HOST, self.slug)
