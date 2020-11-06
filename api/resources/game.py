from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from game.models import Game, GameEvent
from ..serializers import GameSerializer, GameEventSerializer


class GameResource(APIView):
    def post(self, request):
        """ Creates a new game """

        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameSingleResource(APIView):
    def get(self, request, game_id):
        """ Returns a game serialized or not found """

        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GameEventResource(APIView):
    def get(self, request, game_id):
        """ Returns a list of all game events """
        events = GameEvent.objects.filter(game_id=game_id)
        serializer = GameEventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, game_id):
        """ Creates a new event """

        try:
            Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GameEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
