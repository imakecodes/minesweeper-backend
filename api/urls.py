from django.urls import path

from .resources.main import MainResource
from .resources.game import GameResource, GameSingleResource, GameEventResource


app_name = "api"

urlpatterns = [
    path("games/<game_id>/events", GameEventResource.as_view(), name="games_events"),
    path("games/<game_id>", GameSingleResource.as_view(), name="games_single"),
    path("games", GameResource.as_view(), name="games"),
    path("", MainResource.as_view(), name="main"),
]
