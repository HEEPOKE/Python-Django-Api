from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


class ListUser(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializers_class = UserSerializer


class CreateUser(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializers_class = UserSerializer


class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializers_class = UserSerializer


class DeleteUser(generics.DestroyAPIView):
    queryset = UserModel.objects.all()
    serializers_class = UserSerializer
