from rest_framework import viewsets
from movimentacoes.api import serializers
from movimentacoes import models

class MovimentacaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MovimentacaoSerializer
    queryset = models.Movimentacao.objects.all()