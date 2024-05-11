from urllib.parse import urlparse

from django.contrib import admin

from apps.shortener.models import ShortUrl


@admin.register(ShortUrl)
class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ("slug", "created_at", "updated_at", "host")
    ordering = ("-created_at",)

    def host(self, instance):
        parsed_uri = urlparse(instance.url)
        return f"{parsed_uri.scheme}://{parsed_uri.netloc}/"
