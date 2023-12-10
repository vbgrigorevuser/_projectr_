from rest_framework import serializers
from .models import Client, Research, Restaurant

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'phone')

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'client', 'name', 'income', 'wastes')

class ResearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Research
        fields = ('id', 'client', 'profit')