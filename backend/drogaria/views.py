from django.http import JsonResponse
from .models import Venda
from django.shortcuts import render
from .models import Produto, ItemOrcamento, Orcamento
from .models import Orcamento
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, ItemPedido, Produto, Fornecedor
from .forms import PedidoForm, ItemPedidoForm, ItemOrcamentoForm


def finalizar_venda(request, orcamento_id):
    if request.method == 'POST':
        orcamento = Orcamento.objects.get(id=orcamento_id)
        forma_pagamento = request.POST.get('forma_pagamento')
        desconto = request.POST.get('desconto', 0)
        entrega = request.POST.get('entrega')

        venda = Venda.objects.create(
            orcamento=orcamento,
            forma_pagamento=forma_pagamento,
            desconto=desconto,
            entrega=entrega
        )

        # Exclui o orçamento após a venda
        orcamento.delete()

        return JsonResponse({'status': 'success', 'venda_id': venda.id})

    return render(request, 'drogaria/orcamentos/finalizar_venda.html', {'orcamento_id': orcamento_id})


def orcamentos_index(request):
    """
    Página inicial de orçamentos, onde os produtos e valores podem ser gerenciados.
    """
    return render(request, "drogaria/orcamentos/orcamentos_index.html", {})

def orcamentos(request):
    orcamento = None
    form = ItemOrcamentoForm()

    if request.method == "POST":
        form = ItemOrcamentoForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            # Relaciona o item ao orçamento atual
            item.orcamento = orcamento
            item.save()
            return redirect('orcamentos:orcamentos_index')

    context = {
        'form': form,
        'orcamento': orcamento,
    }
    return render(request, 'drogaria/orcamentos/orcamentos_index.html', context)


def compras(request):
    """
    Exibe a página de compras.
    """
    return render(request, "drogaria/compras/compras_index.html", {})


def adicionar_item(request):
    """
    Adiciona um item ao orçamento.
    """
    if request.method == "POST":
        produto_id = request.POST.get("produto_id")
        quantidade = int(request.POST.get("quantidade", 1))
        desconto = float(request.POST.get("desconto", 0.0))
        orcamento_id = request.POST.get("orcamento_id")

        try:
            # Recupera ou cria o orçamento
            orcamento, created = Orcamento.objects.get_or_create(id=orcamento_id)

            # Recupera o produto
            produto = Produto.objects.get(id=produto_id)

            # Calcula o valor unitário com base no preço do produto
            valor_unitario = produto.preco

            # Cria o item no orçamento
            item = ItemOrcamento.objects.create(
                orcamento=orcamento,
                produto=produto,
                quantidade=quantidade,
                valor_unitario=valor_unitario,
                desconto=desconto,
            )

            # Atualiza o valor total do orçamento
            orcamento.valor_total += item.subtotal()
            orcamento.save()

            return JsonResponse({
                "status": "success",
                "message": "Item adicionado com sucesso."
            })

        except Produto.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Produto não encontrado."
            })
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            })

    return JsonResponse({
        "status": "error",
        "message": "Método inválido."
    })

def compras_index(request):
    pedidos = Pedido.objects.all()
    return render(request, 'drogaria/compras/compras_index.html', {'pedidos': pedidos})

def novo_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.save()
            return redirect('compras:lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'drogaria/compras/form_pedido.html', {'form': form})

def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('compras:lista_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'drogaria/compras/form_pedido.html', {'form': form})

def lancar_entrada(request):
    if request.method == "POST":
        # Implementar lógica de registro da nota fiscal
        pass
    return render(request, 'drogaria/compras/form_entrada.html')
