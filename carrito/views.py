from django.shortcuts import redirect
from productos.models import Producto
from django.contrib import messages
from .carrito import Carrito



def AgregarProducto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.Agregar(producto=producto)
    messages.success(request, F"Producto agregado al carrito de compras")
    return redirect("carrito")



def EliminarProducto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.Eliminar(producto)
    messages.success(request, F"Producto eliminado del carrito de compras")
    return redirect("carrito")



def DecrementarProducto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.Decrementar(producto=producto)
    messages.success(request, F"Producto eliminado del carrito de compras")
    return redirect("carrito")



def LimpiarCarrito(request):
    carrito = Carrito(request)
    carrito.clear()
    return redirect("carrito")

