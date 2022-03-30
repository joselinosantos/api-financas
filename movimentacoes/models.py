from django.db import models
from uuid import uuid4

class Movimentacao(models.Model):
    id_movimentacao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=(('e', 'Entrada'), ('s', 'Saída')))
    data = models.DateField()
    create_at = models.DateField(auto_now_add=True)