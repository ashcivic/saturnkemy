from rest_framework import serializers
from .models import ItemOrcamento

class ItemOrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrcamento
        fields = "__all__"
