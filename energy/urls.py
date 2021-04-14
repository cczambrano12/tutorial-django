from django.conf.urls import url
from django.urls import include, path
from .routers import router
from .views import EnergyViewSet


retrieve_params = EnergyViewSet.as_view({
    'get': 'retrieve_by_params',
})

urlpatterns = [
    path('new', retrieve_params),
    url('', include(router.urls)),
]