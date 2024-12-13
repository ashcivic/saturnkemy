# notas_fiscais/views.py

from django.shortcuts import render, redirect
from .models import NFE, NFSe, Configuracao

def nfe_create(request):
    if request.method == 'POST':
        # Process the form to create an NFE
        pass
    return render(request, 'notas_fiscais/nfe/nfe_form.html')

def nfse_create(request):
    if request.method == 'POST':
        # Process the form to create an NFSe
        pass
    return render(request, 'notas_fiscais/nfse/nfse_form.html')

def configuracoes(request):
    if request.method == 'POST':
        # Process the form to update configurations
        pass
    return render(request, 'notas_fiscais/configuracoes/configuracoes_form.html')