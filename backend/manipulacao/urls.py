from django.urls import path
from . import views

app_name = "manipulacao"


urlpatterns = [
    # Orçamentos
    path('orcamentos/', views.orcamentos_index, name='orcamentos_index'),
    path('orcamentos/novo/', views.novo_orcamento, name='novo_orcamento'),
    path('orcamentos/editar/<int:orcamento_id>/', views.editar_orcamento, name='editar_orcamento'),
    
    # Fórmulas
    path('formulas/', views.formulas_index, name='formulas_index'),
    path('formulas/nova/', views.nova_formula, name='nova_formula'),
    path('formulas/manipular/<int:formula_id>/', views.manipular_formula, name='manipular_formula'),
    
    # Pedidos
    path('pedidos/', views.pedidos_index, name='pedidos_index'),
    path('pedidos/novo/', views.novo_pedido, name='novo_pedido'),
    
    # Relatórios
    path('relatorios/', views.relatorios_index, name='relatorios_index'),
    
    # Configurações
    path('configuracoes/usuario/', views.configurar_usuario, name='configurar_usuario'),

]
