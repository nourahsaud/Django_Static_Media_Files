from asyncio import tasks
from django.contrib import admin
from .models import Task, Project
# Register your models here.

admin.site.register(Project)
admin.site.register(Task)