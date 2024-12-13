from django.urls import path
from . import views

app_name = "entregas"

urlpatterns = [
    path('', views.delivery_index, name='delivery_index'),
    path('consultas/', views.consultas_index, name='consultas_index'),
]