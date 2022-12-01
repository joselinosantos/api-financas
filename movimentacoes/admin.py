from django.contrib import admin
from .models import Movimentacao

class Movimentacoes(admin.ModelAdmin):
    list_display = ['id_movimentacao', 'descricao', 'valor', 'tipo', 'categoria', 'data']
    list_display_links = ['id_movimentacao', 'descricao']

admin.site.register(Movimentacao, Movimentacoes)