import django_filters
from .models import Entrega  # Substitua pelo seu modelo real, se necessário

class EntregaFilter(django_filters.FilterSet):
    # Filtros baseados nos campos do modelo Entrega
    # Aqui, você pode adicionar filtros personalizados conforme necessário

    data_entrega = django_filters.DateFilter(field_name='data_entrega', lookup_expr='exact', label='Data de Entrega')  # Filtra por data exata
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains', label='Status')  # Filtra por status, com busca parcial
    entregador = django_filters.CharFilter(field_name='entregador__nome', lookup_expr='icontains', label='Entregador')  # Filtro de entregador pelo nome (assumindo que existe uma relação)
    responsavel = django_filters.CharFilter(field_name='responsavel__nome', lookup_expr='icontains', label='Responsável')  # Filtro por responsável, se houver uma relação

    # Se quiser um filtro por intervalo de datas, você pode usar:
    data_inicio = django_filters.DateFilter(field_name='data_entrega', lookup_expr='gte', label='Data Início')
    data_fim = django_filters.DateFilter(field_name='data_entrega', lookup_expr='lte', label='Data Fim')

    class Meta:
        model = Entrega  # Nome do seu modelo
        fields = ['data_entrega', 'status', 'entregador', 'responsavel']  # Campos que você quer permitir no filtro
