from rest_framework import serializers
from metas import models

class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meta
        fields = '__all__'