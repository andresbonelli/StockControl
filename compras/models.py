from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    dni = models.IntegerField(max_length=8, null=False, unique=True, primary_key=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}, DNI: {self.dni}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    precio = models.DecimalField(decimal_places=2, max_digits=10, max_length=10)
    stock_actual = models.IntegerField(max_length=8, null=False)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
