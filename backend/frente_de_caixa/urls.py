# apps/frente_de_caixa/urls.py
from django.urls import path
from . import views

app_name='frente_de_caixa'

urlpatterns = [
    path('caixas/', views.caixas, name='caixas'),
    path('console/', views.console, name='console'),
    path('solicitar-acao/<int:caixa_id>/', views.solicitar_acao, name='solicitar_acao'),
]
