from django.contrib import admin
from .models import Meta

class Metas(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'valor', 'data_inicial', 'data_final', 'status']
    list_display_links = ['id', 'descricao']

admin.site.register(Meta, Metas)
