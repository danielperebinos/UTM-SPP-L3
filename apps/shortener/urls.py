from django.urls import path

from apps.shortener.views import CreateShortUrlView

urlpatterns = [
    path("generate", CreateShortUrlView.as_view(), name="shortly"),
]
