from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from rest_framework.generics import CreateAPIView

from apps.shortener.models import ShortUrl
from apps.shortener.serializers import ShortUrlSerializer


class CreateShortUrlView(CreateAPIView):
    serializer_class = ShortUrlSerializer


class RedirectToRealSourceView(RedirectView):
    permanent = True

    def get_redirect_url(self, key: str):
        short_url = get_object_or_404(ShortUrl, slug=key)
        return short_url.url
