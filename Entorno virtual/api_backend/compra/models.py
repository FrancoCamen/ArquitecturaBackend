from django.db import models

# Create your models here.


class Cliente(models.Model):
    dni = models.IntegerField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=15, null=False, blank=False)
    direccion = models.CharField(max_length=20)
    correo = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} - {self.dni}"

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15, null=False, blank=False)
    descripcion = models.CharField(max_length=40)
    total = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.nombre}"  
    

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    total = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, blank=True)

    def __str__(self):
        return f"{self.fecha} - {self.total}"
    
