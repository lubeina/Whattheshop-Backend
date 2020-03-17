from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import UserCreateSerializer, CakeSerializer, CartSerializer, Cart_ItemSerializer, ProfileSerializer
from .models import Cake, Cart_Item, Cart
from django.contrib.auth.models import User


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ProfileDetails(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile


class CakeList(ListAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer


class CartDetail(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user, active=True)


class CartItem(CreateAPIView):
    serializer_class = Cart_ItemSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
