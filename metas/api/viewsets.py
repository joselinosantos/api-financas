from rest_framework import viewsets
from metas.api import serializers
from metas import models

class MetaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MetaSerializer
    queryset = models.Meta.objects.all()