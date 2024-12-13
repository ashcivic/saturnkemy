# notas_fiscais/urls.py

from django.urls import path
from .views import nfe_create, nfse_create, configuracoes

app_name='notas_fiscais'

urlpatterns = [
    path('nfe/', nfe_create, name='nfe_create'),
    path('nfse/', nfse_create, name='nfse_create'),
    path('configuracoes/', configuracoes, name='configuracoes'),
]