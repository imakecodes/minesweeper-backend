from rest_framework import serializers

from game.models import Game, GameEvent


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = ["board"]


class GameEventSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["active_game"] = GameSerializer(instance.game).data
        return response

    class Meta:
        model = GameEvent
        fields = "__all__"
