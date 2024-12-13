from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    codigo_barras = models.CharField(max_length=100, blank=True, null=True)
    codigo_interno = models.CharField(max_length=100, unique=True)
    unidade_medida = models.CharField(max_length=10)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Saida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    motivo = models.TextField()
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data_saida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"

class Inventario(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_fisica = models.DecimalField(max_digits=10, decimal_places=2)
    data_inventario = models.DateTimeField(auto_now_add=True)
