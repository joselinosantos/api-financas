from rest_framework import serializers
from contas import models

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conta
        fields = '__all__'