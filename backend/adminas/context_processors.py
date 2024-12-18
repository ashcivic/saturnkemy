from .models import DadosEmpresa

def dados_empresa(request):
    dados = DadosEmpresa.objects.first()
    return {"dados_empresa": dados}
