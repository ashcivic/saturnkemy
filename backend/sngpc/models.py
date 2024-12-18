from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    codigo_barras = models.CharField(max_length=50, unique=True)
    registro_ms = models.CharField(max_length=20)
    lote = models.CharField(max_length=50)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.codigo_barras}"

class ConfiguracaoSngpc(models.Model):
    ambiente = models.CharField(
        max_length=20,
        choices=[("homologacao", "Homologação"), ("producao", "Produção")],
        default="homologacao"
    )

    def __str__(self):
        return f"Ambiente: {self.get_ambiente_display()}"
    
class XML(models.Model):
    nome = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to="xmls/")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome