from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),  # noqa E501
    path('accounts/', include('backend.accounts.urls')),  # noqa E501
    path('bookstore/', include('backend.bookstore.urls', namespace='bookstore')),  # noqa E501
    path('crm/', include('backend.crm.urls', namespace='crm')),  # noqa E501
    path('expense/', include('backend.expense.urls', namespace='expense')),  # noqa E501
    path('product/', include('backend.product.urls', namespace='product')),  # noqa E501
    path('todo/', include('backend.todo.urls', namespace='todo')),  # noqa E501
    path('admin/', admin.site.urls),  # noqa E501
    path('sngpc/', include('backend.sngpc.urls', namespace='sngpc')),# noqa E501
    path('drogaria/', include('backend.drogaria.urls', namespace='drogaria')),# noqa E501
    path('cadastros/', include('backend.cadastros.urls', namespace='cadastros')), # noqa E501
    path('notas_fiscais/', include('backend.notas_fiscais.urls', namespace='otas_fiscais')), # noqa E501
    path('manipulacao/', include('backend.manipulacao.urls', namespace='manipulacao')), # noqa E501
    path('financeiro/', include('backend.financeiro.urls', namespace='financeiro')), # noqa E501
    path('gestao_estoque/', include('backend.gestao_estoque.urls', namespace='gestao_estoque')), # noqa E501
    path('entregas/', include('backend.entregas.urls', namespace='entregas')), # noqa E501
    path('gestor/', include('backend.gestor.urls', namespace='gestor')), # noqa E501
    path('frente_de_caixa/', include('backend.frente_de_caixa.urls', namespace='frente_de_caixa')) # noqae501
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Adicionando URLs de media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)