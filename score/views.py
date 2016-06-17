from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HighScore
from .serializers import HighScoreSerializer


class ScoreList(APIView):
    def get(self, request):
        print("GET method is requested !")
        scores = HighScore.objects.all()
        serializer = HighScoreSerializer(scores, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("POST method is requested !")
        serializer = HighScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        print("DELETE method is requested !")
        score = HighScore.objects.get(pk=pk)
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
