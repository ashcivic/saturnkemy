# apps/frente_de_caixa/views.py
from django.shortcuts import render, get_object_or_404
from .models import Caixa, FormaPagamento, SolicitarAcao

def caixas(request):
    caixas = Caixa.objects.all()
    return render(request, 'frente_de_caixa/caixas.html', {'caixas': caixas})

def console(request):
    formas_pagamento = FormaPagamento.objects.all()
    return render(request, 'frente_de_caixa/console.html', {'formas_pagamento': formas_pagamento})


def solicitar_acao(request, caixa_id):
    caixa = get_object_or_404(Caixa, id=caixa_id)
    if request.method == 'POST':
        acao = request.POST.get('acao')
        SolicitarAcao.objects.create(caixa=caixa, acao=acao)
    return render(request, 'frente_de_caixa/solicitar_acao.html', {'caixa': caixa})