from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import UserCreateSerializer, CakeSerializer, CartSerializer, CartItemCreateSerializer, ProfileSerializer, CartSerializer
from .models import Cake, Cart_Item, Cart
from django.contrib.auth.models import User

from rest_framework.permissions import (IsAuthenticated)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ProfileDetails(RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user


class CakeList(ListAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer


class CartDetail(RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        cart,created = Cart.objects.get_or_create(user=self.request.user, active=True)
        return cart


class CartItem(CreateAPIView):
    serializer_class = CartItemCreateSerializer

    def perform_create(self, serializer):
        cart,created = Cart.objects.get_or_create(user=self.request.user, active=True)
        serializer.save(cart = cart)




class Checkout(APIView):
    def get(self, request):
        cart = Cart.objects.get(user=request.user, active=True)
        cart.active = False
        cart.save()
        return Response({"whatever":"whatever you want to return"})

