from django.urls import path

from .resources.main import MainResource


app_name = "api"

urlpatterns = [path("", MainResource.as_view(), name="main")]
