from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("autenticación.urls")),
    path('', include("usuario.urls")),
    path('', include("productos.urls")),
    path('', include("carrito.urls")),
    path('', include("orden.urls")),
]
