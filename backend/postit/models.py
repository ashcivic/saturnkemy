from django.db import models
from django.contrib.auth import get_user_model

# Obtendo o modelo de usuário personalizado
User = get_user_model()

class PostIt(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    cor = models.CharField(max_length=7, default='#FFFF00')  # Hexadecimal para cor (exemplo: amarelo)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Usando o modelo de usuário personalizado
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
