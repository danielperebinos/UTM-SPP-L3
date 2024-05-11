from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from drf_util.decorators import serialize_decorator
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.shortener.models import ShortUrl
from apps.shortener.serializers import UrlSerializer, ShortUrlSerializer
from apps.shortener.utils import Encoder


class ShortenerView(APIView):
    @serialize_decorator(UrlSerializer)
    def post(self, request):
        if request.valid and (url := request.valid.get("url")):
            key = Encoder.retrive_key(url)
            short_url, created = ShortUrl.objects.get_or_create(
                slug=key, url=url
            )

            return Response(ShortUrlSerializer(short_url).data, status=201)


class RedirectToRealSourceView(RedirectView):
    permanent = True

    def get_redirect_url(self, key: str):
        short_url = get_object_or_404(ShortUrl, slug=key)
        return short_url.url
