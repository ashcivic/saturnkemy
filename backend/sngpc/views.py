from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .services import SNGPCService
from .models import Inventario
from .utils import gerar_xml_inventario, compactar_e_converter_base64, calcular_md5
import requests


def sngpc_list(request):
    ambiente = 'producao' if request.GET.get('ambiente') == 'producao' else 'homologacao'
    if request.method == 'POST':
        dados = request.POST.get('dados')
        service = SNGPCService(ambiente)
        xml_data = service.gerar_xml(eval(dados))
        status, response = service.enviar_xml(xml_data)
        return HttpResponse(f"Status: {status}, Resposta: {response}")

    return render(request, 'sngpc/sngpc_list.html', {'ambiente': ambiente})


def enviar_inventario(request, inventario_id):
    inventario = Inventario.objects.get(id=inventario_id)
    xml = gerar_xml_inventario(inventario)
    base64_xml = compactar_e_converter_base64(xml)
    hash_md5 = calcular_md5(base64_xml)

    response = requests.post(
        "http://homologacao.anvisa.gov.br/sngpc/webservice/sngpc.asmx/EnviaArquivoSNGPC",
        data={
            "Email": request.user.email,
            "Senha": request.user.senha_sngpc,
            "Arq": base64_xml,
            "Hashindenficacacao": hash_md5
        }
    )

    return JsonResponse({"status": response.text})
