from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HighScore
from .serializers import HighScoreSerializer


class ScoreList(APIView):
    def get(self, request):
        scores = HighScore.objects.all()
        serializer = HighScoreSerializer(scores, many=True)
        return Response(serializer.data)

    def post(self):
        pass
