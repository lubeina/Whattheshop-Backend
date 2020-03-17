from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cake, Cart, Cart_Item
from datetime import date


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name,
                        last_name=last_name, email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    past_items = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'past_items']

    def get_past_items(self, obj):
        items = Cart.objects.filter(user=obj, date__lt=date.today())
        return CartSerializer(items, many=True).data


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ['name', 'image', 'price', 'flavor', 'size', 'shape', 'id']


class CartItemSerializer(serializers.ModelSerializer):
    cake = serializers.SlugRelatedField(slug_field='name', read_only=True)
    item_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart_Item
        fields = ['cake', 'quantity','item_price']
    
    def get_item_price(self, obj):
        return obj.cake.price*obj.quantity


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cart_item = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['user', 'date','cart_item']
    
    def get_cart_item(self, obj):
        cart_item = Cart_Item.objects.filter(cart=obj.id)
        return CartItemSerializer(cart_item, many=True).data

      
class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Item
        fields = ['cake', 'quantity']



