from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'data_criacao', 'data_limite')
    list_filter = ('status', 'data_criacao')
    search_fields = ('titulo', 'descricao')
