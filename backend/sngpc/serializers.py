from rest_framework import serializers

class DadosSNGPCSerializer(serializers.Serializer):
    registro = serializers.CharField(max_length=50)
    tipo = serializers.ChoiceField(choices=['Entrada', 'Saida'])
    produto = serializers.CharField(max_length=100)
    quantidade = serializers.IntegerField()
    data = serializers.DateField()
