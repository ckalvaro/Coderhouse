from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.SmallIntegerField()
    ultimo_asado = models.CharField(max_length=20)
    
