from django.contrib import admin
from .models import Conta

class Contas(admin.ModelAdmin):
    list_display = ['descricao', 'instituicao', 'agencia', 'conta', 'saldo']

admin.site.register(Conta, Contas)
