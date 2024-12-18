from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from backend.sngpc.xml_operations.sngpc_generator import gerar_xml_sngpc
from backend.sngpc.xml_operations.sngpc_validator import validar_xml
from backend.sngpc.xml_operations.sngpc_sender import enviar_xml_sngpc
from .models import Produto, ConfiguracaoSngpc, XML
from backend.adminas.models import DadosEmpresa  # Importando o modelo DadosEmpresa
from django.db.models import Q


@login_required
def listar_xml(request):
    return render(request, "sngpc/sngpc_list.html", {})


@login_required
def sngpc_processar(request):
    if request.method == "POST":
        # Buscar produtos pelo formulário
        codigo_barras = request.POST.get("codigo_barras")
        nome_produto = request.POST.get("nome_produto")

        try:
            produtos = Produto.objects.filter(
                Q(nome__icontains=nome_produto) | Q(codigo_barras=codigo_barras)
            )
        except Produto.DoesNotExist:
            return JsonResponse({"status": "Erro", "mensagem": "Produto não encontrado"})

        # Buscar dados da empresa
        dados_empresa = DadosEmpresa.objects.first()
        if not dados_empresa:
            return JsonResponse(
                {"status": "Erro", "mensagem": "Dados da empresa não cadastrados."}
            )

        # Dados de entrada do XML com informações da empresa
        dados_cabecalho = {
            "cnpjEmissor": dados_empresa.cnpj,
            "cpfTransmissor": dados_empresa.cpf_responsavel,
            "data": "2024-06-10",  # Exemplo estático, pode usar datetime.now()
        }

        medicamentos = []
        for produto in produtos:
            medicamentos.append({
                "classeTerapeutica": "1",
                "registroMSMedicamento": produto.registro_ms,
                "numeroLoteMedicamento": produto.lote,
                "quantidadeMedicamento": str(produto.quantidade),
                "unidadeMedidaMedicamento": "1",
            })

        insumos = []  # Pode ser alimentado similar aos medicamentos

        # Gerar o XML
        try:
            xml_path = gerar_xml_sngpc(dados_cabecalho, medicamentos, insumos)
        except Exception as e:
            return JsonResponse({"status": "Erro", "mensagem": str(e)})

        # Validar XML
        valido, msg_validacao = validar_xml(xml_path)
        if not valido:
            return JsonResponse({"status": "Erro", "mensagem": msg_validacao})

        # Enviar XML
        try:
            resposta = enviar_xml_sngpc(xml_path)
        except Exception as e:
            return JsonResponse({"status": "Erro", "mensagem": str(e)})

        return JsonResponse({"status": "Sucesso", "resposta": resposta})

    return render(request, "sngpc/sngpc_list.html")


@login_required
def buscar_produtos(request):
    query = request.GET.get("q", "").strip()
    if len(query) < 3:
        return JsonResponse([], safe=False)

    produtos = Produto.objects.filter(
        Q(nome__icontains=query) | Q(codigo_barras__icontains=query)
    )[:10]

    resultados = [
        {
            "nome": produto.nome,
            "codigo_barras": produto.codigo_barras,
            "quantidade": produto.quantidade or "",  # Adapte conforme sua base
            "lote": produto.lote or "",  # Adapte conforme sua base
        }
        for produto in produtos
    ]
    return JsonResponse(resultados, safe=False)


@login_required
def deletar_xml(request, xml_id):
    """
    View para deletar um XML.
    """
    xml = get_object_or_404(XML, id=xml_id)

    if request.method == "POST":
        xml.delete()
        messages.success(request, "XML deletado com sucesso!")
        return redirect("sgnpc/sngpc_list.html")

    messages.error(request, "A exclusão deve ser confirmada.")
    return redirect("sgnpc/sngpc_list.html")
