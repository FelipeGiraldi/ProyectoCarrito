from django.db import models
from django.contrib.auth.models import User


class CuentaCliente(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    rut = models.CharField(primary_key=True,max_length=12)
    nombre_completo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono=models.IntegerField(default=0)
    correo = models.EmailField(max_length=50, unique=True)    
    cupo_credito = models.FloatField(max_length=10,default=2000000)
    puntos = models.IntegerField(default=0) 
    estado =models.CharField(max_length=12,default="Activo") 
    acepta_email = models.BooleanField(verbose_name="Acepta envio de mail")
    
    
    def __str__(self):
        return self.rut

    class Meta:
        db_table = 'CuentaCliente'