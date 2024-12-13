# notas_fiscais/models.py

from django.db import models

class NFE(models.Model):
    pedido_id = models.CharField(max_length=100)
    data_emissao = models.DateTimeField(auto_now_add=True)
    # Add additional fields as needed

class NFSe(models.Model):
    formula_id = models.CharField(max_length=100)
    data_emissao = models.DateTimeField(auto_now_add=True)
    # Add additional fields as needed

class Configuracao(models.Model):
    certificado = models.FileField(upload_to='certificados/')
    senha = models.CharField(max_length=100)
    ambiente = models.CharField(max_length=20, choices=[('homologacao', 'Homologação'), ('producao', 'Produção')])
    # Add additional configuration fields as needed