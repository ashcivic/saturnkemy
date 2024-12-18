from django.contrib import admin
from .models import Venda, Pagina, Promocao, KitProduto, Material

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'cliente', 'valor', 'data_venda', 'status')
    list_filter = ('status', 'data_venda')
    search_fields = ('produto', 'cliente')

@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'ativa')
    list_filter = ('ativa',)
    search_fields = ('titulo',)

@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'desconto_percentual', 'data_inicio', 'data_fim', 'ativa')
    list_filter = ('ativa', 'data_inicio', 'data_fim')
    search_fields = ('descricao',)

@admin.register(KitProduto)
class KitProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'desconto_percentual')
    search_fields = ('nome',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')
    search_fields = ('titulo',)
