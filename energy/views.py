from .models import Energy_generation
from rest_framework import permissions
from .serializers import EnergySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .services import get_energy
from django.http import JsonResponse

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
class EnergyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Energy_generation.objects.all()
    serializer_class = EnergySerializer
    permission_classes = [permissions.AllowAny]


    def retrieve_by_params(self, request, *args, **kwargs):
        latitude = request.GET.get('lat', 0)
        longitude = request.GET.get('lon', 0)
        tilt = request.GET.get('tilt', 0)
        power = request.GET.get('power', 0)

        energy_data = get_energy(latitude, longitude, tilt, power)
        logger.info(energy_data)

        new_data = Energy_generation(**energy_data)
        logger.info(new_data)
        new_data.save()
        logger.info(new_data.id)

        return JsonResponse(energy_data)