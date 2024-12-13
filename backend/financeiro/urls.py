from django.urls import path
from . import views

app_name='financeiro'

urlpatterns = [
    path('contas-a-pagar/', views.contas_a_pagar, name='contas_a_pagar'),
    path('contas-a-receber/', views.contas_a_receber, name='contas_a_receber'),
    path('cadastros/', views.cadastros, name='cadastros'),
    path('contabilidade/', views.contabilidade, name='contabilidade'),
]
