from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('A Fazer', 'A Fazer'), ('Em Progresso', 'Em Progresso'), ('Feito', 'Feito')])
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_limite = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class KanbanColumn(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

class Card(models.Model):
    PRIORITY_CHOICES = [
        ('BAIXA', 'Baixa'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    ]

    column = models.ForeignKey(KanbanColumn, related_name='cards', on_delete=models.CASCADE)
    content = models.TextField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='MEDIA')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Card ({self.content[:20]}...) in {self.column.title}"