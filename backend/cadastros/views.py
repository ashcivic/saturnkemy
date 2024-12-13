# cadastros/views.py


from .models import Cliente, Convenio, Representante, Fornecedor
import requests
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, redirect

class CNPJConsultView(View):
    def get(self, request, cnpj):
        # Remove caracteres não numéricos do CNPJ
        cnpj = ''.join(filter(str.isdigit, cnpj))

        # Verifica se o CNPJ tem exatamente 14 dígitos
        if len(cnpj) != 14:
            return JsonResponse({'status': 'ERROR', 'message': 'CNPJ inválido'}, status=400)

        # Faz a requisição à API da ReceitaWS
        response = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}', headers={'Accept': 'application/json'})

        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({'status': 'ERROR', 'message': 'CNPJ não encontrado'}, status=404)
        
# Clientes Views (already created in previous code)
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/clientes/cliente_list.html', {'clientes': clientes})

class ClienteCreateView(View):
    def get(self, request):
        return render(request, 'cadastros/clientes/cliente_form.html')  # Renderiza o formulário

    def post(self, request):
        # Captura todos os campos do formulário
        nome_fantasia = request.POST.get('fantasia')
        razao_social = request.POST.get('nome')
        endereco = request.POST.get('logradouro')
        inscricao_estadual = request.POST.get('inscricao_estadual')  # Se você tiver esse campo
        uf = request.POST.get('uf')
        responsavel = request.POST.get('responsavel')  # Se você tiver esse campo
        telefone = request.POST.get('telefone')
        whatsapp = request.POST.get('whatsapp')  # Se você tiver esse campo
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        
        # Campos do CNPJ
        cnpj = request.POST.get('cnpj')
        tipo = request.POST.get('tipo')
        porte = request.POST.get('porte')
        abertura = request.POST.get('abertura')
        atividade_principal = request.POST.get('atividade_principal')
        natureza_juridica = request.POST.get('natureza_juridica')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        municipio = request.POST.get('municipio')
        situacao = request.POST.get('situacao')
        data_situacao = request.POST.get('data_situacao')
        motivo_situacao = request.POST.get('motivo_situacao')
        situacao_especial = request.POST.get('situacao_especial')
        data_situacao_especial = request.POST.get('data_situacao_especial')
        capital_social = request.POST.get('capital_social')
        simples_optante = request.POST.get('simples_optante') == 'on'  # Verifica se o checkbox foi marcado
        simei_optante = request.POST.get('simei_optante') == 'on'  # Verifica se o checkbox foi marcado

        # Cria o cliente no banco de dados
        cliente = Cliente(
            nome_fantasia=nome_fantasia,
            razao_social=razao_social,
            endereco=endereco,
            inscricao_estadual=inscricao_estadual,
            uf=uf,
            telefone=telefone,
            email=email,
            cep=cep,
            cnpj=cnpj,
            tipo=tipo,
            porte=porte,
            abertura=abertura,
            atividade_principal=atividade_principal,
            natureza_juridica=natureza_juridica,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            municipio=municipio,
            situacao=situacao,
            data_situacao=data_situacao,
            motivo_situacao=motivo_situacao,
            situacao_especial=situacao_especial,
            data_situacao_especial=data_situacao_especial,
            capital_social=capital_social,
            simples_optante=simples_optante,
            simei_optante=simei_optante,
        )
        cliente.save()  # Salva o cliente no banco de dados

        return redirect('cadastros:cliente_list')  # Redireciona para a lista de clientes

def cliente_create(request):
    if request.method == 'POST':
        documento_tipo = request.POST.get('documento_tipo')
        numero_documento = request.POST.get('numero_documento')
        nome_fantasia = request.POST.get('nome_fantasia')
        razao_social = request.POST.get('razao_social')
        endereco = request.POST.get('endereco')
        inscricao_estadual = request.POST.get('inscricao_estadual', '')
        inscricao_municipal = request.POST.get('inscricao_municipal', '')
        uf = request.POST.get('uf')
        responsavel = request.POST.get('responsavel')
        telefone = request.POST.get('telefone')
        whatsapp = request.POST.get('whatsapp', '')
        email = request.POST.get('email')
        cep = request.POST.get('cep')

        Cliente.objects.create(
            documento_tipo=documento_tipo,
            numero_documento=numero_documento,
            nome_fantasia=nome_fantasia,
            razao_social=razao_social,
            endereco=endereco,
            inscricao_estadual=inscricao_estadual,
            inscricao_municipal=inscricao_municipal,
            uf=uf,
            responsavel=responsavel,
            telefone=telefone,
            whatsapp=whatsapp,
            email=email,
            cep=cep
        )
        return redirect('cliente_list')
    return render(request, 'cadastros/clientes/cliente_form.html')


def convenio_list(request):
    convenios = Convenio.objects.all()
    return render(request, 'cadastros/convenios/convenio_list.html', {'convenios': convenios})

def convenio_create(request):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=request.POST.get('cliente'))
        data_cobranca = request.POST.get('data_cobranca')
        valor_credito = request.POST.get('valor_credito')
        tipo_cobranca = request.POST.get('tipo_cobranca')
        margem = request.POST.get('margem')
        tipo_convenio = request.POST.get('tipo_convenio')

        Convenio.objects.create(
            cliente=cliente,
            data_cobranca=data_cobranca,
            valor_credito=valor_credito,
            tipo_cobranca=tipo_cobranca,
            margem=margem,
            tipo_convenio=tipo_convenio
        )
        return redirect('convenio_list')
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/convenios/convenio_form.html', {'clientes': clientes})

def convenio_edit(request, pk):
    convenio = Convenio.objects.get(pk=pk)
    if request.method == 'POST':
        convenio.cliente = Cliente.objects.get(id=request.POST.get('cliente'))
        convenio.data_cobranca = request.POST.get('data_cobranca')
        convenio.valor_credito = request.POST.get('valor_credito')
        convenio.tipo_cobranca = request.POST.get('tipo_cobranca')
        convenio.margem = request.POST.get('margem')
        convenio.tipo_convenio = request.POST.get('tipo_convenio')
        convenio.save()
        return redirect('convenio_list')
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/convenios/convenio_form.html', {'clientes': clientes, 'convenio': convenio})

def representante_list(request):
    representantes = Representante.objects.all()
    return render(request, 'cadastros/representante/representante_list.html', {'representantes': representantes})

def representante_create(request):
    if request.method == 'POST':
        cliente = Cliente.objects.get(id=request.POST.get('cliente'))
        data_pagamento = request.POST.get('data_pagamento')
        forma_pagamento = request.POST.get('forma_pagamento')
        percentual_pago = request.POST.get('percentual_pago')
        status = request.POST.get('status')

        Representante.objects.create(
            cliente=cliente,
            data_pagamento=data_pagamento,
            forma_pagamento=forma_pagamento,
            percentual_pago=percentual_pago,
            status=status
        )
        return redirect('representante_list')
    clientes = Cliente.objects.all()
    return render(request, 'cadastros/representante/representante_form.html', {'clientes': clientes})

def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'cadastros/fornecedores/fornecedor_list.html', {'fornecedores': fornecedores})

def fornecedor_create(request):
    if request.method == 'POST':
        documento_tipo = request.POST.get('documento_tipo')
        numero_documento = request.POST.get('numero_documento')
        valor_credito_limite = request.POST.get('valor_credito_limite')
        observacoes = request.POST.get('observacoes')
        data_pagamento = request.POST.get('data_pagamento')
        tipos_pagamento = request.POST.get('tipos_pagamento')

        Fornecedor.objects.create(
            documento_tipo=documento_tipo,
            numero_documento=numero_documento,
            valor_credito_limite=valor_credito_limite,
            observacoes=observacoes,
            data_pagamento=data_pagamento,
            tipos_pagamento=tipos_pagamento
        )
        return redirect('fornecedor_list')
    return render(request, 'cadastros/fornecedores/fornecedor_form.html')