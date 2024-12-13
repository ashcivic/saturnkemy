# apps/frente_de_caixa/admin.py
from django.contrib import admin
from .models import Caixa, FormaPagamento, SolicitarAcao

@admin.register(Caixa)
class CaixaAdmin(admin.ModelAdmin):
    list_display = ('id', 'operador', 'total_vendas', 'status', 'data_abertura')
    list_filter = ('status', 'data_abertura')
    search_fields = ('operador__username',)

@admin.register(FormaPagamento)
class FormaPagamentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('tipo',)

@admin.register(SolicitarAcao)
class SolicitarAcaoAdmin(admin.ModelAdmin):
    list_display = ('acao', 'caixa', 'data_solicitacao')
    list_filter = ('acao', 'data_solicitacao')
