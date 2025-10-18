from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import User as CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Serializer for displaying and updating user details."""
    class Meta:
        model = get_user_model()
        fields = [
            'id', 'username', 'email', 'first_name',
            'last_name', 'bio', 'profile_picture'
        ]
        read_only_fields = ['id']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration using get_user_model().objects.create_user()."""
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = [
            'username', 'email', 'password',
            'first_name', 'last_name', 'bio'
        ]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )


        bio = validated_data.get('bio')
        if bio:
            user.bio = bio
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'following']