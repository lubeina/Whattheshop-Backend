from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import UserCreateSerializer, CakeSerializer, CartSerializer, CartItemCreateSerializer, ProfileSerializer,CartItemSerializer
from .models import Cake, Cart_Item, Cart
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status



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
    def create(self, request, *args, **kwargs):
        serializer = CartItemCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_data = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(CartItemSerializer(new_data).data, status=status.HTTP_201_CREATED, headers=headers)
        
        
    def perform_create(self, serializer):
        cart,created = Cart.objects.get_or_create(user=self.request.user, active=True)
        return serializer.save(cart = cart)

