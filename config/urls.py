from django.contrib import admin
from django.urls import path, include

from apps.shortener.views import RedirectToRealSourceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shortner/', include('apps.shortener.urls')),
    path("<str:key>", RedirectToRealSourceView.as_view(), name="redirect-to-real-source"),
]
