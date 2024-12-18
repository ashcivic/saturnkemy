from django import forms
from .models import Usuario, Grupo, DadosEmpresa

class BackupForm(forms.Form):
    TIPO_BACKUP = [
        ('parcial', 'Parcial'),
        ('total', 'Total'),
        ('periodico', 'Periódico'),
    ]
    tipo = forms.ChoiceField(choices=TIPO_BACKUP, label="Tipo de Backup")

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class DadosEmpresaForm(forms.ModelForm):
    class Meta:
        model = DadosEmpresa
        fields = [
            "cnpj",
            "razao_social",
            "nome_fantasia",
            "endereco",
            "telefone",
            "email",
            "inscricao_estadual",
            "inscricao_municipal",
            "uf", 
            "cep", 
            "tipo",
            "porte",
            "abertura",
            "atividade_principal",
            "natureza_juridica",
            "numero",
            "complemento",
            "bairro",
            "municipio",
            "situacao",
            "data_situacao",
            "motivo_situacao",
            "situacao_especial",
            "data_situacao_especial",
            "capital_social",
            "simples_optante",
            "simei_optante",
        ]