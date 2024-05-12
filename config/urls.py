from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.shortener.views import RedirectToRealSourceView

schema_view = get_schema_view(
    openapi.Info(
        title="URL Shortener API",
        default_version='v1',
        description="This API allows you to shorten long URLs into concise and shareable links. "
                    "With this URL Shortener API, you can generate shortened URLs that redirect to the original long URLs.",
        contact=openapi.Contact(email="daniel.perebinos@gmail.com"),
        license=openapi.License(name="No License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("shortner/", include("apps.shortener.urls")),
    path("<str:key>", RedirectToRealSourceView.as_view(), name="redirect-to-real-source"),
]
