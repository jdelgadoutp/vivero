from django.urls import path
from .Vistas import Registro

urlpatterns = [
    path('Registro/', Registro, name="Registro"),
]