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

    def post(self, request):
        serializer = HighScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
