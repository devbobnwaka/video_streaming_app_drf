from django.shortcuts import render
from .models import User
from rest_framework import generics
from .serializers import (UserSerializer, )

# Create your views here.
class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs): #HTTP -> post
       return self.create(request, *args, **kwargs)

# class LoginAPIView(generics.)