from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto, Tipo, Promociones, Canal



def inicio(request):   
    prod = Producto.objects.filter(id_tipo=2)
    return render(request,'index.html', {"productos":prod})

def productos(request):  
    Tip=Tipo.objects.all() 
    produ = Producto.objects.all()   
    return render(request,'productos.html', {"prod":produ,"tipo":Tip})     

def promociones(request):  
    Can=Canal.objects.all() 
    promo = Promociones.objects.all()   
    return render(request,'promociones.html', {"promo":promo,"Can":Can})   

def carrito(request):
    return render( request, 'widget.html', {})

