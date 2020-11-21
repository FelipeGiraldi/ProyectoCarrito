from django.urls import path, include
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/',productos, name="productos"),
    path('promociones/',promociones, name="promociones"),
    path('carrito/',carrito, name="carrito"),
]


