from django.db import models

class Conta(models.Model):
    descricao = models.TextField()
    instituicao = models.TextField()
    agencia = models.TextField()
    conta = models.TextField()
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
