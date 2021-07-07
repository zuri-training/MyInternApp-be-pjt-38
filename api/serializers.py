from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from.models import *
#from rest_framework.permissions import IsAuthenticated
#from django.db import models
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate
#from django.contrib.auth.hashers import make_password

#Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         Model = User
#         fields = ('id','username','password','first_name','last_name')
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], 
#         password = validated_data['password'],first_name =validated_data['first_name'],
#         last_name=validated_data['last_name']
#         )
#         return user

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'phone')

# User serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'