from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import formCliente
from .models import CuentaCliente
from django.contrib import messages

def registrate(request):  
    if request.method == "POST":
        form = formCliente(request.POST)
        if form.is_valid():
            CuentaCliente = form.save(commit=False)
            CuentaCliente.usuario_id = request.user.id
            CuentaCliente.save()
            rut = form.cleaned_data.get("rut")
            messages.success(request,F"El rut: {rut} se ha creado correctamente")
            return redirect('inicio')

    form = formCliente()  
    return render(request,'registrate.html',{"form":form})




