from django.urls import path
from .views import sngpc_processar, buscar_produtos, listar_xml, deletar_xml
from django.contrib.auth import views as auth_views

app_name='sngpc'

urlpatterns = [
    path("sngpc/", listar_xml, name="listar_xml"),
    path("sngpc/processar/", sngpc_processar, name="sngpc_processar"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("buscar-produtos/", buscar_produtos, name="buscar_produtos"),
    path("xmls/deletar/<int:xml_id>/", deletar_xml, name="deletar_xml"),
]
