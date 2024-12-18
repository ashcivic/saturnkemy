from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, F
from .models import ContasPagar, ContasReceber, Vendas, Entregas

# Biblioteca para gráficos (exemplo com Chart.js)
import json

def dashboard(request):
    # Coletando dados para os gráficos

    # 1. Gráfico de Contas a Pagar e a Receber
    contas_pagar = ContasPagar.objects.aggregate(total=Sum('valor'))['total'] or 0
    contas_receber = ContasReceber.objects.aggregate(total=Sum('valor'))['total'] or 0

    # 2. Gráfico de Vendas por mês
    vendas_por_mes = (
        Vendas.objects.annotate(mes=F('data__month'))
        .values('mes')
        .annotate(total=Sum('valor'))
        .order_by('mes')
    )
    vendas_labels = [item['mes'] for item in vendas_por_mes]
    vendas_data = [item['total'] for item in vendas_por_mes]

    # 3. Gráfico de Custos com Entregas
    custos_entregas = (
        Entregas.objects.aggregate(total=Sum('custo'))['total'] or 0
    )

    # Dados para os gráficos (exemplo com Chart.js)
    data = {
        "contas": {
            "labels": ["Contas a Pagar", "Contas a Receber"],
            "data": [contas_pagar, contas_receber],
        },
        "vendas": {
            "labels": vendas_labels,
            "data": vendas_data,
        },
        "entregas": custos_entregas,
    }

    return render(request, 'dashboard.html', {"data": json.dumps(data)})
