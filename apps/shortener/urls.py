from django.urls import path

from apps.shortener.views import ShortenerView

urlpatterns = [
    path("generate", ShortenerView.as_view(), name="shortly")
]