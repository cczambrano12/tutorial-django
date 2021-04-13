from django.urls import path
from . import views

urlpatterns = [
    path('fecha', views.hello_time),
    path('<int:year>/', views.hello_year),
    path('json/<slug:data>/', views.json_data, name='json data'),
]