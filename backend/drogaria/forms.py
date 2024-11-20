from django import forms
from .models import ItemOrcamento, Orcamento
from .models import Pedido, ItemPedido

class ItemOrcamentoForm(forms.ModelForm):
    class Meta:
        model = ItemOrcamento
        fields = ['produto', 'quantidade', 'valor_unitario', 'desconto']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['status']

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade_pedida']
