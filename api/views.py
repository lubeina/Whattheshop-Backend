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

    def post(self, request):
        serializer = CakeCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, cake_id):
        cake = Cake.objects.get(id=cake_id)
        serializer = CakeCreateSerializer(cake, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cake_id):
        cake = Cake.objects.get(id=cake_id)
        cake.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CakesList(ListAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
