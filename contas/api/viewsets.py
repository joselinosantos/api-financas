from rest_framework import viewsets
from contas.api import serializers
from contas import models

class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContaSerializer
    queryset = models.Conta.objects.all()