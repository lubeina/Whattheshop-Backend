from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, CakeCreateSerializer, CakeSerializer
from .models import Cake
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CakeView(APIView):

    def get(self, request, cake_id=None):
        if cake_id:
            cake = Cake.objects.get(id=cake_id)
            serializer = CakeSerializer(cake)
        else:
            cakes = Cake.objects.all()
            serializer = CakeSerializer(cakes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
