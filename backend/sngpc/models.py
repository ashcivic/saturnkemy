from django.db import models

class EstablishmentConfig(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    nome_farmacia = models.CharField(max_length=100)
    responsavel_tecnico = models.CharField(max_length=100)
    ambiente = models.CharField(
        max_length=20,
        choices=[("homologacao", "Homologação"), ("producao", "Produção")],
        default="homologacao"
    )
    created_at = models.DateTimeField(auto_now_add=True)

class MedicamentoMovimentacao(models.Model):
    tipo_movimentacao = models.CharField(
        max_length=20,
        choices=[
            ("entrada", "Entrada"),
            ("saida", "Saída"),
            ("perda", "Perda")
        ]
    )
    medicamento = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    data_movimentacao = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)


class RegistroSNGPC(models.Model):
    registro = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10)
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    data = models.DateField()
    status_envio = models.CharField(max_length=20, default='Pendente')
    data_envio = models.DateTimeField(null=True, blank=True)

class Inventario(models.Model):
    cnpj_emissor = models.CharField(max_length=14)
    cpf_transmissor = models.CharField(max_length=11)
    data = models.DateField()

class Medicamento(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, related_name='medicamentos')
    classe_terapeutica = models.IntegerField(choices=[(1, "Antimicrobiano"), (2, "Sujeito a controle especial")])
    registro_ms = models.CharField(max_length=13)
    numero_lote = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    unidade_medida = models.IntegerField(choices=[(1, "Caixas"), (2, "Frascos")])