from django.db import models
from uuid import uuid4

CATEGORIAS = (
    ('1', 'Casa'),
    ('2', 'Transporte'),
    ('3', 'Alimentação'),
    ('4', 'Saúde'),
    ('5', 'Vestuário'),
    ('6', 'Higiene'),
    ('7', 'Judicial'),
    ('8', 'Hobby'))

class Movimentacao(models.Model):
    id_movimentacao = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=(('e', 'Entrada'), ('s', 'Saída')))
    categoria = models.CharField(max_length=1, choices=CATEGORIAS)
    data = models.DateField()
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.descricao