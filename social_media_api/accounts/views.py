from rest_framework import generics, permissions, response, status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

class RegisterAPIView(generics.CreateAPIView):
  serializer_class = RegisterSerializer
  permission_classes = [permissions.AllowAny]

def create(self, request, *args, **kwargs):
  serializer = self.get_serializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  user = serializer.save()
  token, _ = Token.objects.get_or_create(user=user)
  data = UserSerializer(user, context={'request': request}).data
  return Response({
    'user': data,
    'token': token.key
  }, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
  permission_classes = [permissions.AllowAny]

def post(self, request):
  serializer = LoginSerializer(data=request.data)
  serializer.is_valid(raise_exception=True)
  user = serializer.validated_data['user']
  token, _ = Token.objects.get_or_create(user=user)
  data = UserSerializer(user, context={'request': request}).data
  return Response({'user': data, 'token': token.key})

class ProfileAPIView(generics.RetrieveUpdateAPIView):
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

def get_object(self):
  return self.request.user

class FollowToggleAPIView(APIView):
  permission_classes = [permissions.IsAuthenticated]

def post(self, request, username):
  target = get_object_or_404(User, username=username)
  user = request.user
  if target == user:
    return Response({'detail': "You can't follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
  if user in target.followers.all():
    target.followers.remove(user)
    return Response({'detail': 'unfollowed'})
  else:
    target.followers.add(user)
    return Response({'detail': 'followed'})
  
