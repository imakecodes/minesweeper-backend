from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("", include("api.urls")),
]

# We need this only for development purpose
if settings.DEBUG is True:
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]
