from django.urls import path
from . import views

app_name='adminas'

urlpatterns = [
    path('usuarios/', views.pag_gest, name='pag_gest'),
    path('adicionar/', views.adicionar_usuarios, name='adicionar_usuarios'),
    path('usuarios/<int:user_id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('desativar/<int:id>/', views.desativar_usuario, name='desativar_usuario'),
    path('usuarios/<int:user_id>/resetar_senha/', views.resetar_senha, name='resetar_senha'),
    path('permissoes/', views.listar_permissoes, name='listar_permissoes'),
    path('permissoes/configurar/', views.configurar_permissao, name='configurar_permissao'),
    path('backups/', views.listar_backups, name='listar_backups'),
    path('backups/criar/', views.criar_backup, name='criar_backup'),
    path('atualizacoes/verificar/', views.verificar_atualizacoes, name='verificar_atualizacoes'),
]
