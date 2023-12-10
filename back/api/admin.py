from django.contrib import admin
from .models import Client, Research, Restaurant

# Register your models here.
admin.site.register(Client)
admin.site.register(Research)
admin.site.register(Restaurant)