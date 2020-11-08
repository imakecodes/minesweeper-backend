from rest_framework import serializers

from game.models import Game, GameEvent, GameStatuses


class GameSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        response = super().to_representation(instance)
        if not response["status"] == GameStatuses.FINISHED:
            del response["board"]

        return response

    class Meta:
        model = Game
        fields = "__all__"


class GameEventSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["active_game"] = GameSerializer(instance.game).data
        return response

    class Meta:
        model = GameEvent
        fields = "__all__"
