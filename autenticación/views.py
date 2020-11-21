from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from usuario.models import CuentaCliente


def acceder(request):   
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_user = form.cleaned_data.get("username")
            password_user = form.cleaned_data.get("password")
            usuario= authenticate(username=nombre_user,password=password_user)
            if usuario is not None:
                login(request,usuario)
                messages.success(request,F"Bienvenida de nuevo: {nombre_user}")
                #revisar si el usuario existe en Cuenta Cliente
                if CuentaCliente.objects.filter(usuario_id=request.user.id): 
                    return redirect('inicio')
                #caso contrario redirigir a que ingrese sus datos
                else:
                    return redirect('usuario')
            else:
                messages.error(request,"Los datos son incorrectos")
        else:
            messages.error(request,"Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request,'acceder.html', {"form":form})

class vistaRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request,'registro.html', {"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usu=form.save()
            nombre_user = form.cleaned_data.get("username")
            messages.success(request,F"Bienvenida a la plataforma: {nombre_user}")
            login(request,usu)
            return redirect('usuario')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
                return render(request,'registro.html', {"form":form})
    
def salir(request):
    logout(request)
    messages.success(request,F"Tu sesión se a cerrado correctamente")
    return redirect('acceder')            




    