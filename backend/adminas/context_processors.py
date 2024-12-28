from django.core.cache import cache
from .models import DadosEmpresa

def dados_empresa(request):
    empresa = cache.get("dados_empresa")
    if not empresa:
        empresa = DadosEmpresa.objects.first()
        cache.set("dados_empresa", empresa, 60 * 60)  # Cache por 1 hora
    return {"dados_empresa": empresa}