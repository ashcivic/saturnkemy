from django.contrib import admin
from .models import Produto, Orcamento, ItemOrcamento
from .models import Fornecedor, Produto, Pedido, ItemPedido

# Registro do modelo Produto
#@admin.register(Produto)  # Registro único usando o decorador
#class ProdutoAdminOrcamentos(admin.ModelAdmin):
#    list_display = ['nome', 'preco_venda', 'quantidade_disponivel']  # Exemplo para Orçamentos
#    search_fields = ['nome']

# Registro do modelo Orcamento
@admin.register(Orcamento)  # Registro único usando o decorador
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'valor_total', 'data_criacao']
    search_fields = ['cliente__nome']

    def cliente(self, obj):
        return obj.cliente.nome if obj.cliente else "Cliente não identificado"
    cliente.short_description = 'Cliente'

    def valor_total(self, obj):
        return obj.valor_total
    valor_total.short_description = 'Valor Total'

    def data_criacao(self, obj):
        return obj.data_criacao.strftime('%d/%m/%Y %H:%M')
    data_criacao.short_description = 'Data de Criação'

# Registro do modelo ItemOrcamento
@admin.register(ItemOrcamento)  # Registro único usando o decorador
class ItemOrcamentoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'valor_unitario', 'desconto', 'subtotal']

    def subtotal(self, obj):
        return obj.subtotal()
    subtotal.short_description = 'Subtotal'

    def produto(self, obj):
        return obj.produto.nome
    produto.short_description = 'Produto'

    def quantidade(self, obj):
        return obj.quantidade
    quantidade.short_description = 'Quantidade'

    def valor_unitario(self, obj):
        return obj.valor_unitario
    valor_unitario.short_description = 'Valor Unitário'

    def desconto(self, obj):
        return obj.desconto
    desconto.short_description = 'Desconto'

# Não é necessário registrar novamente, pois já usamos o decorador `@admin.register`
# admin.site.register(Produto, ProdutoAdmin)  # Não deve ser duplicado
# admin.site.register(Orcamento, OrcamentoAdmin)  # Não deve ser duplicado
# admin.site.register(ItemOrcamento, ItemOrcamentoAdmin)  # Não deve ser duplicado


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'telefone', 'email']

#@admin.register(Produto)
# Classe ProdutoAdmin para o módulo Compras
#class ProdutoAdminCompras(admin.ModelAdmin):
#    list_display = ['nome', 'quantidade_estoque', 'preco_compra']  # Exemplo para Compras
#    search_fields = ['nome']
#    list_filter = ['fornecedor']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'status', 'data_pedido', 'ultima_atualizacao']

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'produto', 'quantidade_pedida', 'quantidade_recebida', 'data_lancamento']

class ProdutoAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        if "compras" in request.path:
            return ['nome', 'quantidade_estoque', 'preco_compra']
        elif "orcamentos" in request.path:
            return ['nome', 'preco_venda', 'quantidade_disponivel']
        return super().get_list_display(request)

admin.site.register(Produto, ProdutoAdmin)
