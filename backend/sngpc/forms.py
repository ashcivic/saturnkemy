from django import forms

class DadosSNGPCForm(forms.Form):
    registro = forms.CharField(max_length=50)
    tipo = forms.ChoiceField(choices=[('Entrada', 'Entrada'), ('Saida', 'Saída')])
    produto = forms.CharField(max_length=100)
    quantidade = forms.IntegerField()
    data = forms.DateField()
