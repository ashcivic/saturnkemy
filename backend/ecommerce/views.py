from .models import Venda, Pagina, Promocao, Material
from django.shortcuts import render, get_object_or_404, redirect


def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'ecommerce/vendas.html', {'vendas': vendas})

def listar_paginas(request):
    paginas = Pagina.objects.filter(ativa=True)
    return render(request, 'ecommerce/paginas.html', {'paginas': paginas})

def listar_promocoes(request):
    promocoes = Promocao.objects.filter(ativa=True)
    return render(request, 'ecommerce/promocoes.html', {'promocoes': promocoes})

def listar_materiais(request):
    materiais = Material.objects.all()
    return render(request, 'ecommerce/materiais.html', {'materiais': materiais})