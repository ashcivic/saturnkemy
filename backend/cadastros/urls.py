# cadastros/urls.py

from django.urls import path
from .views import (
    cliente_list, cliente_create,
    convenio_list, convenio_create, convenio_edit,
    representante_list, representante_create,
    fornecedor_list, fornecedor_create, CNPJConsultView
)
app_name='cadastros'

urlpatterns = [
    path('consultar-cnpj/<str:cnpj>/', CNPJConsultView.as_view(), name='consultar_cnpj'),
    # Clientes
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/novo/', cliente_create, name='cliente_create'),

    # Convênios
    path('convenios/', convenio_list, name='convenio_list'),
    path('convenios/novo/', convenio_create, name='convenio_create'),
    path('convenios/editar/<int:pk>/', convenio_edit, name='convenio_edit'),

    # Representantes
    path('representantes/', representante_list, name='representante_list'),
    path('representantes/novo/', representante_create, name='representante_create'),

    # Fornecedores
    path('fornecedores/', fornecedor_list, name='fornecedor_list'),
    path('fornecedores/novo/', fornecedor_create, name='fornecedor_create'),
]