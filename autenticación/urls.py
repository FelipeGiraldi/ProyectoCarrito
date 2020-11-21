from django.urls import path, include
from .views import *

urlpatterns = [
    path('registro/', vistaRegistro.as_view(), name="registro"),
    path('acceder/', acceder, name="acceder"),
    path('salir/', salir, name="salir"),
]
