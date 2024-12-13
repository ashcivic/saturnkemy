from django.db import models

class ContaPagar(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    status = models.CharField(
        max_length=50, 
        choices=[('pendente', 'Pendente'), ('paga', 'Paga')],
        default='pendente'
    )

class ContaReceber(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    recebimento = models.DateField()
    status = models.CharField(
        max_length=50, 
        choices=[('pendente', 'Pendente'), ('recebida', 'Recebida')],
        default='pendente'
    )

class ContaBancaria(models.Model):
    banco = models.CharField(max_length=100)
    agencia = models.CharField(max_length=20)
    conta = models.CharField(max_length=20)
    tipo = models.CharField(
        max_length=20,
        choices=[('corrente', 'Corrente'), ('poupança', 'Poupança')],
        default='corrente'
    )

class ArquivoContabilidade(models.Model):
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('entrada', 'Entrada'),
            ('emissao_nfe', 'Emissão NF-e'),
            ('emissao_nfse', 'Emissão NFS-e'),
            ('sat', 'SAT')
        ]
    )
    data_geracao = models.DateField(auto_now_add=True)
    enviado = models.BooleanField(default=False)
