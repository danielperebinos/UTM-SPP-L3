from rest_framework import serializers

from apps.shortener.models import ShortUrl


class UrlSerializer(serializers.Serializer):
    url = serializers.URLField()


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ("shorted", "url", "created_at", "updated_at")
        read_only_fields = ("url", "created_at", "updated_at")
