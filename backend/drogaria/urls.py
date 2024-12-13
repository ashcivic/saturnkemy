from django.urls import path
from . import views

app_name = 'drogaria'

urlpatterns = [
    path('orcamentos/', views.orcamentos, name='orcamentos'),
    path('orcamentos/', views.orcamentos_index, name='orcamentos_index'),
    path('orcamentos/finalizar/<int:orcamento_id>/', views.finalizar_venda, name='finalizar_venda'),
    path("orcamentos/adicionar-item/", views.adicionar_item, name="adicionar_item"),
    path('compras/', views.compras, name='compras'),
    path('compras/', views.compras_index, name='compras_index'),
    #path('', views.lista_pedidos, name='lista_pedidos'),
    path('novo/', views.novo_pedido, name='novo_pedido'),
    path('editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('lancar-entrada/', views.lancar_entrada, name='lancar_entrada'),
]
