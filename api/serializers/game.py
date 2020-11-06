from rest_framework import serializers

from game.models import Game, GameEvent


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class GameEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameEvent
        fields = "__all__"
