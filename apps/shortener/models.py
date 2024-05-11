from urllib.parse import urljoin

from django.db import models


class ShortUrl(models.Model):
    slug = models.SlugField(max_length=8, primary_key=True)
    url = models.URLField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    @property
    def shorted(self):
        from django.conf import settings
        return urljoin(settings.REDIRECT_HOST, self.slug)
