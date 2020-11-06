from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class MainResource(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the game!"}, status=status.HTTP_200_OK)
