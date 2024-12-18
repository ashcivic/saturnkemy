# Models
from django.db import models


class Venda(models.Model):
    produto = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ], default='concluida')

    def __str__(self):
        return f"Venda {self.id} - {self.produto}"

class Pagina(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Promocao(models.Model):
    descricao = models.CharField(max_length=255)
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao

class KitProduto(models.Model):
    nome = models.CharField(max_length=255)
    produtos = models.ManyToManyField(Venda)
    desconto_percentual = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nome

class Material(models.Model):
    titulo = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='materiais/')
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo