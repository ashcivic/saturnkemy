from django.urls import path
from . import views

app_name='tarefas'

urlpatterns = [
    path('tarefas/', views.kanban_view, name='tarefas'),
    path('update_card/', views.update_card, name='update_card'),  # Verifique se o nome é exatamente 'tarefas'.
    path('adicionar', views.create_column, name='create_column'),
    path('create_card', views.create_card, name='create_card'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
    path('exportar/', views.exportar_agenda, name='exportar_agenda'),

]
