from django.contrib import admin
from .models import Tarefa, KanbanColumn, Card

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'data_criacao', 'data_limite')
    list_filter = ('status', 'data_criacao')
    search_fields = ('titulo', 'descricao')

@admin.register(KanbanColumn)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order')
    list_display_links = ('id', 'title', 'order')
    ordering = ('order','id')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'priority', 'column', 'user', 'created_at', 'updated_at')
    list_display_links = ('id', 'content', 'priority', 'column', 'user', 'created_at', 'updated_at')
    list_filter = ('priority', 'column', 'user')
    search_fields = ('content',)
    #list_editable = ('id', 'content', 'priority', 'column', 'user', 'created_at', 'updated_at')