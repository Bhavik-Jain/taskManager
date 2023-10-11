from django.contrib import admin

# Register your models here.
from .models import TasksStore

admin.site.register(TasksStore)