from django.urls import path
from .views import *

app_name = "carrito"

urlpatterns = [
    path('AgregarProducto/<int:producto_id>/', AgregarProducto, name='AgregarProducto'),
    path('EliminarProducto/<int:producto_id>/', EliminarProducto, name='EliminarProducto'),
    path('DecrementarProducto/<int:producto_id>/', DecrementarProducto, name='DecrementarProducto'),
    path('LimpiarCarrito/', LimpiarCarrito, name='LimpiarCarrito'),
]
