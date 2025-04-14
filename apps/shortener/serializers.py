from rest_framework import serializers

from apps.shortener.models import ShortUrl
from apps.shortener.utils import Encoder


class UrlSerializer(serializers.Serializer):
    url = serializers.URLField()


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ("url", "shorted")
        extra_kwargs = {"shorted": {"read_only": True}}

    def create(self, validated_data):
        slug = Encoder.retrive_key(validated_data["url"])
        short_url, created = ShortUrl.objects.get_or_create(slug=slug, url=validated_data["url"])
        return short_url
