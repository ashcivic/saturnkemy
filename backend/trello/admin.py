from django.contrib import admin

# Register your models here.
from .models import TaskList, Card

admin.site.register(TaskList)
admin.site.register(Card)
