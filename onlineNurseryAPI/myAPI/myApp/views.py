from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import UserSerializer,NurserySerializer
from .models import User,Nursery


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer



class NurseryViewSet(viewsets.ModelViewSet):
    queryset = Nursery.objects.all().order_by('name')
    serializer_class = NurserySerializer