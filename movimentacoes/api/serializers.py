from rest_framework import serializers
from movimentacoes import models

class MovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movimentacao
        fields = '__all__'