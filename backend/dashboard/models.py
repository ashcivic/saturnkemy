from django.db import models

# Modelo para Contas a Pagar
class ContasPagar(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data_vencimento = models.DateField(verbose_name="Data de Vencimento")
    pago = models.BooleanField(default=False, verbose_name="Pago?")

    def __str__(self):
        return f"{self.descricao} - {'Pago' if self.pago else 'Pendente'}"

# Modelo para Contas a Receber
class ContasReceber(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    data_recebimento = models.DateField(verbose_name="Data de Recebimento")
    recebido = models.BooleanField(default=False, verbose_name="Recebido?")

    def __str__(self):
        return f"{self.descricao} - {'Recebido' if self.recebido else 'Pendente'}"

# Modelo para Vendas
class Vendas(models.Model):
    produto = models.CharField(max_length=255, verbose_name="Produto")
    quantidade = models.IntegerField(verbose_name="Quantidade")
    valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Total")
    data = models.DateField(verbose_name="Data da Venda")

    def __str__(self):
        return f"{self.produto} - {self.data}"

# Modelo para Entregas
class Entregas(models.Model):
    entregador = models.CharField(max_length=255, verbose_name="Entregador")
    custo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Custo")
    destino = models.CharField(max_length=255, verbose_name="Destino")
    data_entrega = models.DateField(verbose_name="Data da Entrega")

    def __str__(self):
        return f"{self.entregador} - {self.destino} - {self.data_entrega}"
