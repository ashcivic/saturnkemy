from django.urls import path
from . import views

app_name='gestao_estoque'

urlpatterns = [
    path('inventario/', views.inventario_index, name='inventario_index'),
    path('entradas/', views.entradas_index, name='entradas_index'),
    path('saidas/', views.saidas_index, name='saidas_index'),
    path('', views.listar_produtos, name='listar_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('saida/', views.registrar_saida, name='registrar_saida'),
    path('exportar/', views.exportar_produtos, name='exportar_produtos'),
    path('importar/', views.importar_produtos, name='importar_produtos'),
    
]


