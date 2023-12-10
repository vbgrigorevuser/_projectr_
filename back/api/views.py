from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer, ResearchSerializer, RestaurantSerializer
from .models import Client, Research, Restaurant
# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('last_name')
    serializer_class = ClientSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer

class ResearchViewSet(viewsets.ModelViewSet):
    queryset = Research.objects.all().order_by('profit')
    serializer_class = ResearchSerializer