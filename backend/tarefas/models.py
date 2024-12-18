from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done')])
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_limite = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo
