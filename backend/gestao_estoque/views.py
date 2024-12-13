from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Saida
from .forms import ProdutoForm, SaidaForm
import pandas as pd
from django.http import HttpResponse
from django.contrib import messages


def listar_produtos(request):
    produtos = Produto.objects.filter(ativo=True)
    return render(request, 'gestao_estoque/listar_produtos.html', {'produtos': produtos})

def entradas_index(request):
    return render(request, 'gestao_estoque/entrada_index.html')

def saidas_index(request):
    return render(request, 'gestao_estoque/saida_index.html')

def inventario_index(request):
    return render(request, 'gestao_estoque/inventario_index.html')


def cadastrar_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_produtos')
    return render(request, 'gestao_estoque/cadastrar_produto.html', {'form': form})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('listar_produtos')
    return render(request, 'gestao_estoque/editar_produto.html', {'form': form})

def registrar_saida(request):
    form = SaidaForm(request.POST or None)
    if form.is_valid():
        saida = form.save(commit=False)
        produto = saida.produto
        produto.quantidade -= saida.quantidade
        produto.save()
        saida.save()
        return redirect('listar_produtos')
    return render(request, 'gestao_estoque/registrar_saida.html', {'form': form})

def exportar_produtos(request):
    produtos = Produto.objects.all().values('nome', 'codigo_barras', 'codigo_interno', 'unidade_medida', 'quantidade', 'valor')
    df = pd.DataFrame(produtos)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="produtos.xlsx"'
    df.to_excel(response, index=False)
    return response

def importar_produtos(request):
    if request.method == 'POST' and request.FILES['arquivo']:
        arquivo = request.FILES['arquivo']
        try:
            df = pd.read_excel(arquivo)
            for _, row in df.iterrows():
                produto, _ = Produto.objects.get_or_create(codigo_interno=row['codigo_interno'])
                produto.nome = row['nome']
                produto.codigo_barras = row.get('codigo_barras', None)
                produto.unidade_medida = row['unidade_medida']
                produto.quantidade = row['quantidade']
                produto.valor = row['valor']
                produto.save()
            messages.success(request, "Produtos importados com sucesso.")
        except Exception as e:
            messages.error(request, f"Erro ao importar produtos: {e}")
        return redirect('listar_produtos')
    return render(request, 'gestao_estoque/importar_produtos.html')
