from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from movimentacoes.api import viewsets as movimentacoesviewsets
from metas.api import viewsets as metasviewsets
from contas.api import viewsets as contasviewsets

route = routers.DefaultRouter()
route.register(r'movimentacoes', movimentacoesviewsets.MovimentacaoViewSet, basename="Movimentacao")
route.register(r'metas', metasviewsets.MetaViewSet, basename="Meta")
route.register(r'contas', contasviewsets.ContaViewSet, basename="Conta")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
