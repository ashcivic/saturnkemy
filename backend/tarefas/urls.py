from django.urls import path
from . import views

app_name='tarefas'

urlpatterns = [
    path('tarefas/', views.listar_tarefas, name='tarefas'),  # Verifique se o nome é exatamente 'tarefas'.
    path('tarefas/adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('exportar/', views.exportar_agenda, name='exportar_agenda'),

]
