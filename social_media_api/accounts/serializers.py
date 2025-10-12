from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['followers']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
     model = User
     fields = ['username', 'email', 'password', 'first_name', 'last_name', 'bio']

    def create(self, validated_data):
       password = validated_data.pop('password')
       user = User(**validated_data)
       user.set_password(password)
       user.save()
       Token.objects.create(user=user)
       return user
    
    class LoginSerializer(serializers.Serializer):
       username = serializers.CharField()
       password = serializers.CharField(write_only=True)

    def validate(self, data):
       user = authenticate(username=data.get('username'), password=data.get('password'))
       if not user:
          raise serializers.ValidationError('Invalid credentials')
       data['user'] = user
       return data
     