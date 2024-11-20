from django.shortcuts import render, get_object_or_404, redirect
from .models import Orcamento, Formula, Pedido
from .forms import OrcamentoForm, PedidoForm, FormulaForm, ItemFormulaForm

# Listagem de Orçamentos
def orcamentos_index(request):
    orcamentos = Orcamento.objects.all()
    return render(request, "orcamentos/index.html", {"orcamentos": orcamentos})

# Criar Novo Orçamento
def novo_orcamento(request):
    if request.method == "POST":
        form_orcamento = OrcamentoForm(request.POST)
        if form_orcamento.is_valid():
            orcamento = form_orcamento.save(commit=False)
            orcamento.usuario = request.user
            orcamento.save()
            return redirect("orcamentos_index")
    else:
        form_orcamento = OrcamentoForm()
    return render(request, "orcamentos/novo.html", {"form_orcamento": form_orcamento})

# Editar Orçamento
def editar_orcamento(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, id=orcamento_id)
    if request.method == "POST":
        form_orcamento = OrcamentoForm(request.POST, instance=orcamento)
        if form_orcamento.is_valid():
            form_orcamento.save()
            return redirect("orcamentos_index")
    else:
        form_orcamento = OrcamentoForm(instance=orcamento)
    return render(request, "orcamentos/editar.html", {"form_orcamento": form_orcamento})

# Fórmulas
def formulas_index(request):
    formulas = Formula.objects.all()
    return render(request, "formulas/index.html", {"formulas": formulas})

# Criar Nova Fórmula
def nova_formula(request):
    if request.method == "POST":
        form_formula = FormulaForm(request.POST)
        if form_formula.is_valid():
            form_formula.save()
            return redirect("formulas_index")
    else:
        form_formula = FormulaForm()
    return render(request, "formulas/nova.html", {"form_formula": form_formula})

# Manipular Fórmula
def manipular_formula(request, formula_id):
    formula = get_object_or_404(Formula, id=formula_id)
    if request.method == "POST":
        form_item_formula = ItemFormulaForm(request.POST)
        if form_item_formula.is_valid():
            item_formula = form_item_formula.save(commit=False)
            item_formula.formula = formula
            item_formula.save()
            return redirect("formulas_index")
    else:
        form_item_formula = ItemFormulaForm()
    return render(request, "formulas/manipular.html", {"formula": formula, "form_item_formula": form_item_formula})

# Pedidos
def pedidos_index(request):
    pedidos = Pedido.objects.all()
    return render(request, "pedidos/index.html", {"pedidos": pedidos})

# Criar Novo Pedido
def novo_pedido(request):
    if request.method == "POST":
        form_pedido = PedidoForm(request.POST)
        if form_pedido.is_valid():
            form_pedido.save()
            return redirect("pedidos_index")
    else:
        form_pedido = PedidoForm()
    return render(request, "pedidos/novo.html", {"form_pedido": form_pedido})

# Relatórios
def relatorios_index(request):
    orcamentos = Orcamento.objects.all()
    return render(request, "relatorios/index.html", {"orcamentos": orcamentos})

# Configurações de Usuário
def configurar_usuario(request):
    return render(request, "configuracoes/usuario.html")
