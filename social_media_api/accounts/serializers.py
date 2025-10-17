from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Serializer for displaying and updating user details."""
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'first_name',
            'last_name', 'bio', 'profile_picture'
        ]
        read_only_fields = ['id']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'password',
            'first_name', 'last_name', 'bio'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for handling user login and token retrieval."""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError('Both username and password are required.')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials, please try again.')

        data['user'] = user
        return data
