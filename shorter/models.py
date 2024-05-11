from django.db import models


class ShortenedUrl(models.Model):
    slug = models.SlugField(max_length=8, primary_key=True)
    url = models.URLField(max_length=256)
