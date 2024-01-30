from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ("id", "username", "email", "role", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if validated_data['role'] == 'VE':
            validated_data['is_vendor'] = True
        elif validated_data['role'] == 'CU':
            validated_data['is_customer'] = True
        else:
            validated_data['is_superuser'] = True

        user = User.objects.create_user(**validated_data)
        return user

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}}