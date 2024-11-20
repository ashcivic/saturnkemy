from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField()
    def __str__(self):
        return self.nome

class Orcamento(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Orçamento {self.id} - {self.data_criacao}"

class ItemOrcamento(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def subtotal(self):
        return (self.valor_unitario * self.quantidade) - self.desconto

class Venda(models.Model):
    orcamento = models.OneToOneField(Orcamento, on_delete=models.CASCADE)
    forma_pagamento = models.CharField(max_length=255)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    entrega = models.JSONField(null=True, blank=True)  # Armazena os dados de entrega
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda {self.id} - {self.data_venda}"

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome

#class Produto(models.Model):
    #nome = models.CharField(max_length=255)
    #quantidade_estoque = models.PositiveIntegerField(default=0)

    #def __str__(self):
     #   return self.nome

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Em Aberto'),
        ('comprado', 'Comprado'),
        ('recebido', 'Recebido'),
        ('cancelado', 'Cancelado'),
        ('recebido_parcial', 'Recebido Parcialmente'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='pedidos_criados'
    )
    editado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='pedidos_editados'
    )
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.get_status_display()}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_pedida = models.PositiveIntegerField()
    quantidade_recebida = models.PositiveIntegerField(default=0)
    data_lancamento = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.produto.nome} ({self.quantidade_pedida} pcs)"