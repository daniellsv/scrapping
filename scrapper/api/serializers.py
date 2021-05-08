from rest_framework import serializers
from scrapper.models import diario_as


class diario_asSerializer(serializers.ModelSerializer):
    class Meta:
        model = diario_as
        fields = ['name', 'point']
