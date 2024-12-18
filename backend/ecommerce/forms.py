from django import forms
from .models import Venda, Pagina, Promocao, Material

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'cliente', 'valor', 'status']

class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['titulo', 'conteudo', 'ativa']

class PromocaoForm(forms.ModelForm):
    class Meta:
        model = Promocao
        fields = ['descricao', 'desconto_percentual', 'data_inicio', 'data_fim', 'ativa']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['titulo', 'arquivo', 'descricao']
