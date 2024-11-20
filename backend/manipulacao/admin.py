from django.contrib import admin
from .models import (
    MateriaPrima,
    Formula,
    ItemFormula,
    TextoRotulo,
    Capsula,
    Frasco,
    Orcamento,
    Pedido,  # Adicionando Pedido
    ItemPedido  # Adicionando ItemPedido
)

# Configuração para Materia-Prima
@admin.register(MateriaPrima)
class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'unidade_medida', 'custo_por_unidade']  # 'unidade_medida' no lugar de 'tipo_medida'
    list_filter = ['unidade_medida']  # Filtrando pela 'unidade_medida', e removendo 'tipo_medida'


# Configuração para Fórmulas
class ItemFormulaInline(admin.TabularInline):
    model = ItemFormula
    extra = 1  # Adiciona uma linha em branco no formulário para criação de novos itens


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_criacao", "usuario_criador")
    search_fields = ("nome",)
    inlines = [ItemFormulaInline]  # Adiciona os itens da fórmula dentro da página de Fórmulas
    list_filter = ("data_criacao",)


# Configuração para Textos de Rótulos
@admin.register(TextoRotulo)
class TextoRotuloAdmin(admin.ModelAdmin):
    list_display = ("nome", "conteudo")
    search_fields = ("nome",)


# Configuração para Cápsulas
@admin.register(Capsula)
class CapsulaAdmin(admin.ModelAdmin):
    list_display = ("tipo", "capacidade")
    search_fields = ("tipo",)


# Configuração para Frascos
@admin.register(Frasco)
class FrascoAdmin(admin.ModelAdmin):
    list_display = ("tipo", "capacidade")
    search_fields = ("tipo",)


# Configuração para Orçamentos
class OrcamentoInline(admin.TabularInline):
    model = ItemFormula  # Adiciona os itens da fórmula ao orçamento
    extra = 1  # Adiciona uma linha extra para criar novos itens no orçamento


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'status', 'valor_total', 'data_criacao']  # Adiciona 'valor_total'
    readonly_fields = ['valor_total']  # Define 'valor_total' como somente leitura
    search_fields = ("usuario__username", "id")  # Permite a busca por 'usuario' ou 'id'
    list_filter = ("status", "data_criacao")  # Permite filtrar por 'status' e 'data_criacao'
    inlines = [OrcamentoInline]  # Permite incluir itens no orçamento diretamente na página de orçamento

    # Método para calcular o 'valor_total' do orçamento
    def valor_total(self, obj):
        return obj.custo_total()  # Chama o método custo_total para calcular o valor total do orçamento
    valor_total.short_description = 'Valor Total'


# Configuração para Pedidos
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'status', 'data_pedido', 'ultima_atualizacao')
    list_filter = ('status', 'data_pedido')
    search_fields = ('usuario__username',)

# Configuração para Itens de Pedidos
@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('materia_prima', 'quantidade_solicitada', 'quantidade_recebida')
    search_fields = ('materia_prima__nome',)

#admin.site.register(Formula, F)