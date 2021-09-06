from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre=models.CharField(max_length=200)

class Auto(models.Model):
    patente=models.CharField(max_length=7)
    propietario=models.CharField(max_length=200)
    # id_marca=models.IntegerField()
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE) # muchos es a uno.


