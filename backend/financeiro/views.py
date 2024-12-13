from django.shortcuts import render, redirect
from .models import ContaPagar, ContaReceber, ContaBancaria, ArquivoContabilidade
from .forms import ContaPagarForm, ContaReceberForm, ContaBancariaForm

def contas_a_pagar(request):
    contas = ContaPagar.objects.all()
    if request.method == 'POST':
        form = ContaPagarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contas_a_pagar')
    else:
        form = ContaPagarForm()
    return render(request, 'financeiro/contas_a_pagar/contas_a_pagar.html', {'contas': contas, 'form': form})

def contas_a_receber(request):
    contas = ContaReceber.objects.all()
    if request.method == 'POST':
        form = ContaReceberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contas_a_receber')
    else:
        form = ContaReceberForm()
    return render(request, 'financeiro/contas_a_receber/contas_a_receber.html', {'contas': contas, 'form': form})

def cadastros(request):
    contas_bancarias = ContaBancaria.objects.all()
    if request.method == 'POST':
        form = ContaBancariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastros')
    else:
        form = ContaBancariaForm()
    return render(request, 'financeiro/cadastros/cadastros.html', {'contas_bancarias': contas_bancarias, 'form': form})

def contabilidade(request):
    arquivos = ArquivoContabilidade.objects.filter(enviado=False)
    return render(request, 'financeiro/contabilidade/contabilidade.html', {'arquivos': arquivos})
