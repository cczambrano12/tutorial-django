from django.conf import settings
from rest_framework import serializers
from .models import Energy_generation

class EnergySerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format=settings.DATETIME_FORMAT, read_only=True)

    class Meta:
        model = Energy_generation
        fields = ['latitude', 'longitude', 'energy', 'average_energy', 'year', 'created_date', 'power', 'tilt']
