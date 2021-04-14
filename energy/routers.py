from .views import EnergyViewSet
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'data', EnergyViewSet)
