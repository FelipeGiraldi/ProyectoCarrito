from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Order, OrderLine
from carrito.carrito import Carrito


# Create your views here.
@login_required(login_url='/autenticacion/acceder')
def process_order(request):
    order = Order.objects.create(user=request.user, completed=True)
    carrito = Carrito(request)
    order_lines = list()
    for key, value in carrito.carrito.items():
        order_lines.append(
            OrderLine(
                product_id=key,
                quantity=value["cantidad"],
                user=request.user,
                order=order
            )
        )

    OrderLine.objects.bulk_create(order_lines)


    carrito.Limpiar()

    messages.success(request, "El pedido se ha creado correctamente!")
    return redirect("listadoOrden")





class OrderList(ListView):
    model = Order
    ordering = ["-id"]
    template_name = "listadoOrden.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class OrderDetail(DetailView):
    model = Order
    template_name = "detalle.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)