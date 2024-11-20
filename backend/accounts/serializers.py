from rest_framework import serializers
from .models import Entrega  # Substitua por seus modelos reais

class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = '__all__'  # Inclui todos os campos do modelo
        # Ou use `fields = ('campo1', 'campo2')` para especificar campos
