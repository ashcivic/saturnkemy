# apps/frente_de_caixa/models.py
from django.db import models
from django.conf import settings

class Caixa(models.Model):
    operador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='operadores')
    total_vendas = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_dinheiro = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_credito = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_debito = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_pix = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_convenio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('aberto', 'Aberto'), ('fechado', 'Fechado')], default='aberto')

    def __str__(self):
        return f"Caixa {self.id} - Operador: {self.operador.username}"


class SolicitarAcao(models.Model):
    acao = models.CharField(max_length=20, choices=[('sangria', 'Sangria'), ('pausa', 'Pausa'), ('fechamento', 'Fechamento')])
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE, related_name='solicitacoes')
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitação {self.acao} para o Caixa {self.caixa.id}"

class FormaPagamento(models.Model):
    tipo = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo
