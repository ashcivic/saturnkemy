# URLS
from django.urls import path
from . import views

app_name='ecommerce'

urlpatterns = [
    path('vendas/', views.listar_vendas, name='listar_vendas'),
    path('paginas/', views.listar_paginas, name='listar_paginas'),
    path('promocoes/', views.listar_promocoes, name='listar_promocoes'),
    path('materiais/', views.listar_materiais, name='listar_materiais'),
]
