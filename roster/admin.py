from django.contrib import admin
from .models import Client, ClassType, ClassSession

admin.site.register(Client)
admin.site.register(ClassType)
admin.site.register(ClassSession)
