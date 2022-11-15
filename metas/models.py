from django.db import models

class Meta(models.Model):
    STATUS = (
        ('1', 'Andamento'),
        ('2', 'Cancelada'),
        ('3', 'Concluída'),
    )

    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicial = models.DateField()
    data_final = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS)
