from django import forms
from usuario.models import CuentaCliente

class formCliente(forms.ModelForm):
    class Meta:
        model = CuentaCliente
        fields = ('rut','nombre_completo','direccion','telefono','correo','cupo_credito','puntos','estado','acepta_email')
    
    
