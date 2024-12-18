# Configuração do Ap
from django.apps import AppConfig
default_auto_field = 'django.db.models.BigAutoField'
class EcommerceConfig(AppConfig):
    default_auto_field = default_auto_field
    name = 'backend.ecommerce'
    verbose_name = 'E-commerce'