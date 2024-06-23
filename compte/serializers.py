from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Profile

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = Profile
        fields = ('email', 'username', 'password', 'first_name', 'last_name')


class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = Profile
        fields = ('email', 'username', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active', 'is_staff']
