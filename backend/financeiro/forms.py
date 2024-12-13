from django import forms
from .models import ContaPagar, ContaReceber, ContaBancaria, ArquivoContabilidade

class ContaPagarForm(forms.ModelForm):
    class Meta:
        model = ContaPagar
        fields = '__all__'

class ContaReceberForm(forms.ModelForm):
    class Meta:
        model = ContaReceber
        fields = '__all__'

class ContaBancariaForm(forms.ModelForm):
    class Meta:
        model = ContaBancaria
        fields = '__all__'
