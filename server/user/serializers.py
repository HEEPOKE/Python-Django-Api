from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelsSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'username', 'password', 'createdAt', 'updatedAt')
        
