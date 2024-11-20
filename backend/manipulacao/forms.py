from django import forms
from .models import Orcamento, ItemOrcamento, MateriaPrima, Formula, Pedido, ItemPedido, Capsula, Frasco, TextoRotulo, ItemFormula

# Formulário para MateriaPrima
class MateriaPrimaForm(forms.ModelForm):
    class Meta:
        model = MateriaPrima
        fields = ['nome', 'unidade_medida', 'custo_por_unidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'unidade_medida': forms.TextInput(attrs={'class': 'form-control'}),
            'custo_por_unidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulário para Formula
class FormulaForm(forms.ModelForm):
    class Meta:
        model = Formula
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# Formulário para ItemFormula (relacionado com Formula)
class ItemFormulaForm(forms.ModelForm):
    class Meta:
        model = ItemFormula
        fields = ['formula', 'materia_prima', 'quantidade']
        widgets = {
            'formula': forms.Select(attrs={'class': 'form-control'}),
            'materia_prima': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulário para Orcamento
class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['usuario', 'status', 'cliente']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulário para ItemOrcamento (relacionado com Orcamento)
class ItemOrcamentoForm(forms.ModelForm):
    class Meta:
        model = ItemOrcamento
        fields = ['orcamento', 'materia_prima', 'quantidade', 'valor_unitario']
        widgets = {
            'orcamento': forms.Select(attrs={'class': 'form-control'}),
            'materia_prima': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulário para Pedido
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario', 'status', 'ultima_atualizacao']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'ultima_atualizacao': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

# Formulário para ItemPedido (relacionado com Pedido)
class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido', 'materia_prima', 'quantidade_solicitada', 'quantidade_recebida']
        widgets = {
            'pedido': forms.Select(attrs={'class': 'form-control'}),
            'materia_prima': forms.Select(attrs={'class': 'form-control'}),
            'quantidade_solicitada': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantidade_recebida': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulário para Capsula
class CapsulaForm(forms.ModelForm):
    class Meta:
        model = Capsula
        fields = ['tipo', 'capacidade']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulário para Frasco
class FrascoForm(forms.ModelForm):
    class Meta:
        model = Frasco
        fields = ['tipo', 'capacidade']
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulário para TextoRotulo
class TextoRotuloForm(forms.ModelForm):
    class Meta:
        model = TextoRotulo
        fields = ['nome', 'conteudo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

