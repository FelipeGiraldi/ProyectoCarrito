from django.db import models

class Tipo(models.Model):
        id = models.IntegerField(primary_key=True)
        descripcion = models.CharField(max_length=50)

        def __str__(self):
            return self.descripcion

        class Meta:
            db_table = 'Tipo'

class Producto(models.Model):
        id = models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length=50)
        especificacion = models.CharField(max_length=100, blank=True, null= True)
        stock=models.IntegerField(default=0) 
        precio_venta=models.FloatField(max_length=10,default=0)
        img = models.CharField(max_length=50)
        id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

        def __str__(self):
                return self.nombre

        class Meta:
                db_table = 'Producto'

class Canal(models.Model):
        descripcion = models.CharField(max_length=50)

        def __str__(self):
            return self.descripcion

        class Meta:
                db_table = 'Canal'

class Promociones(models.Model):
        especificacion = models.CharField(max_length=100)
        fec_ini = models.DateTimeField(auto_now_add=True)
        fec_fin = models.DateField(max_length=20)
        precio_nuevo = models.FloatField(max_length=20, default=0)
        stock=models.IntegerField(default=0) 
        estado = models.CharField(max_length=12, default="Vigente") 
        img = models.CharField(max_length=50)   
        producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
        canal = models.ForeignKey(Canal, on_delete=models.CASCADE)

        def __str__(self):
            return (self.nombre)
        
        class Meta:
                db_table = 'Promociones'
