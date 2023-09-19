from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_entre = models.DateField()
    entregado = models.BooleanField()