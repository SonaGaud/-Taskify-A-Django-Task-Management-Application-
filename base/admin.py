from django.contrib import admin
from .models import Task # imported Task function from models.py
# Register our model with admin panel
admin.site.register(Task)