# cadastros/models.py

from django.db import models

class Cliente(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    inscricao_estadual = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cep = models.CharField(max_length=10)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    porte = models.CharField(max_length=50, blank=True, null=True)
    abertura = models.DateField(blank=True, null=True)
    atividade_principal = models.CharField(max_length=255, blank=True, null=True)
    natureza_juridica = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=50, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    situacao = models.CharField(max_length=50, blank=True, null=True)
    data_situacao = models.DateField(blank=True, null=True)
    motivo_situacao = models.CharField(max_length=255, blank=True, null=True)
    situacao_especial = models.CharField(max_length=255, blank=True, null=True)
    data_situacao_especial = models.DateField(blank=True, null=True)
    capital_social = models.CharField(max_length=50, blank=True, null=True)
    simples_optante = models.BooleanField(default=False)
    simei_optante = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_fantasia


class Convenio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_cobranca = models.DateField()
    valor_credito = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_cobranca = models.CharField(max_length=20)
    margem = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_convenio = models.CharField(max_length=20)

    def __str__(self):
        return f"Convênio: {self.cliente.nome_fantasia}"


class Representante(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    forma_pagamento = models.CharField(max_length=20)
    percentual_pago = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
        ('cancelado', 'Cancelado'),
        ('bloqueado', 'Bloqueado'),
    ])

    def __str__(self):
        return f"Representante: {self.cliente.nome_fantasia}"


class Fornecedor(models.Model):
    DOCUMENTO_CHOICES = [
        ('CNPJ', 'CNPJ'),
        ('CPF', 'CPF'),
    ]

    documento_tipo = models.CharField(max_length=4, choices=DOCUMENTO_CHOICES)
    numero_documento = models.CharField(max_length=18)
    valor_credito_limite = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)
    data_pagamento = models.DateField()
    tipos_pagamento = models.CharField(max_length=20)

    def __str__(self):
        return f"Fornecedor: {self.numero_documento}"