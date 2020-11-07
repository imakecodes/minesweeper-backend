from rest_framework import serializers

from game.models import Game, GameEvent


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = ["board"]


class GameEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameEvent
        fields = "__all__"
