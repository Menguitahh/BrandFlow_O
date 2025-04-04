from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import *

class UserSerializerView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # queryset = User.objects.all()