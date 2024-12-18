from django.urls import path
from . import views

app_name='postit'

urlpatterns = [
    path('postits/', views.listar_postits, name='postits'),
    path('postits/adicionar/', views.adicionar_postit, name='adicionar_postit'),
    path('postits/editar/<int:id>/', views.editar_postit, name='editar_postit'),
    path('postits/excluir/<int:id>/', views.excluir_postit, name='excluir_postit'),
]
