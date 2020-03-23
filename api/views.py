from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .serializers import UserCreateSerializer, CakeSerializer, CartSerializer, CartItemCreateSerializer, ProfileSerializer,CartItemSerializer,CartUpdateSerializer
from .models import Cake, CartItem, Cart
from .permissions import IsCartOwner

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

class DeleteCartItem(DestroyAPIView):
	queryset = CartItem.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'cartitem_id'
	permission_classes = [IsAuthenticated, IsCartOwner]

class UpdateCart(RetrieveUpdateAPIView):
    serializer_class = CartUpdateSerializer
    queryset = CartItem.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'cartitem_id'
    permission_classes = [IsAuthenticated, IsCartOwner]

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





