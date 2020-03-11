from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cake


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
