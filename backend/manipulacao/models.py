from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Classe de Matéria Prima
class MateriaPrima(models.Model):
    nome = models.CharField(max_length=255)
    custo_por_unidade = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    unidade_medida = models.TextField()

    def __str__(self):
        return self.nome

# Classe de Cápsula
class Capsula(models.Model):
    nome = models.CharField(max_length=255)
    tamanho = models.CharField(max_length=100)
    cor = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    tipo = models.TextField()
    capacidade = models.TextField()

    def __str__(self):
        return f'{self.nome} - {self.tamanho}'

# Classe de Frasco
class Frasco(models.Model):
    nome = models.CharField(max_length=255)
    capacidade = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f'{self.nome} - {self.capacidade_ml}ml'

# Classe de Texto Rótulo
class TextoRotulo(models.Model):
    conteudo = models.TextField()
    frasco = models.ForeignKey(Frasco, related_name='textos_rotulo', on_delete=models.CASCADE)
    nome = models.TextField()

    def __str__(self):
        return f'Texto para {self.frasco.nome}'

# Classe de Fórmula
class Formula(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario_criador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
# Classe de Orçamento
class Orcamento(models.Model):
    STATUS_CHOICES = [
        ('A', 'Aberto'),
        ('F', 'Fechado'),
        ('C', 'Cancelado'),
    ]
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    cliente = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Orçamento {self.id} - {self.cliente}"

# Classe de Item de Fórmula
class ItemFormula(models.Model):
    formula = models.ForeignKey(Orcamento, on_delete=models.CASCADE, related_name='itens')
    materia_prima = models.ForeignKey('MateriaPrima', on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.materia_prima.nome} - {self.quantidade}"


# Classe de Item de Orçamento
class ItemOrcamento(models.Model):
    orcamento = models.ForeignKey(Orcamento, related_name='itens', on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Item {self.id} do Orçamento {self.orcamento.id}"

# Classe de Pedido de Compra
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('A', 'Aberto'),
        ('F', 'Fechado'),
        ('C', 'Cancelado'),
    ]
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    data_pedido = models.DateTimeField(auto_now_add=True)
    fornecedor = models.CharField(max_length=255)
    ultima_atualizacao = models.DateTimeField()
    
    def __str__(self):
        return f'Pedido {self.id} - {self.fornecedor}'

# Classe de Item de Pedido
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    quantidade_solicitada = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_recebida = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return f'Item {self.id} do Pedido {self.pedido.id}'
