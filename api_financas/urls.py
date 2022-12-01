from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from movimentacoes.api import viewsets as movimentacoesviewsets
from metas.api import viewsets as metasviewsets
from contas.api import viewsets as contasviewsets
from rest_framework_swagger.views import get_swagger_view

route = routers.DefaultRouter()
route.register(r'movimentacoes', movimentacoesviewsets.MovimentacaoViewSet, basename="Movimentacao")
route.register(r'metas', metasviewsets.MetaViewSet, basename="Meta")
route.register(r'contas', contasviewsets.ContaViewSet, basename="Conta")

schema_view = get_swagger_view(title='API Minhas Finanças')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(route.urls))
    path('', schema_view),
    path(r'movimentacoes', movimentacoesviewsets.MovimentacaoViewSet.as_view({'get': 'list'})),
    path(r'metas', metasviewsets.MetaViewSet.as_view({'get': 'list'})),
    path(r'contas', contasviewsets.ContaViewSet.as_view({'get': 'list'}))
]
