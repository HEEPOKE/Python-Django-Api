from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializers_class = UserSerializer


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializers_class = UserSerializer


class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializers_class = UserSerializer


class DeleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializers_class = UserSerializer
