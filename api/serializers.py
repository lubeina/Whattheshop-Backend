from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cake, Cart, Cart_Item


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ['name', 'image', 'price', 'flavor', 'size', 'shape', 'id']


class Cart_ItemSerializer(serializers.ModelSerializer):
    cake = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Cart_Item
        fields = ['cake', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    cart_item = Cart_ItemSerializer()
    cart_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['user', 'cart_item', 'cart_total', 'active']

    def get_cart_total(self, obj):
        return obj.cart_item.cake.price*obj.cart_item.quantity
