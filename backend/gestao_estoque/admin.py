from django.contrib import admin
from .models import Produto, Saida, Inventario

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_barras', 'quantidade', 'valor', 'ativo')
    search_fields = ('nome', 'codigo_barras')

@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'data_saida', 'motivo')
    list_filter = ('data_saida',)
