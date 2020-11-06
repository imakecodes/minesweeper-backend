from django.urls import path

from .resources.main import MainResource
from .resources.game import GameResource


app_name = "api"

urlpatterns = [
    path("games", GameResource.as_view(), name="games"),
    path("", MainResource.as_view(), name="main"),
]
