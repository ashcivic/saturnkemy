from django.contrib import admin
from .models import ConfiguracaoSngpc

@admin.register(ConfiguracaoSngpc)
class ConfiguracaoSngpcAdmin(admin.ModelAdmin):
    list_display = ("ambiente",)  # Define o campo a ser exibido
    list_display_links = None  # Remove links de edição direta
    list_editable = ("ambiente",)  # Permite editar o campo diretamente na lista
    actions = None  # Desativa as ações padrão (como deletar)
