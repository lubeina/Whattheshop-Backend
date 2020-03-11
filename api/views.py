from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, CakeSerializer
from .models import Cake


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class CakeList(ListAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer
