# apps/frente_de_caixa/forms.py
from django import forms
from .models import SolicitarAcao

class SolicitarAcaoForm(forms.ModelForm):
    class Meta:
        model = SolicitarAcao
        fields = ['acao']
        widgets = {
            'acao': forms.Select(attrs={'class': 'form-control'}),
        }
