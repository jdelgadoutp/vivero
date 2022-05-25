from django.db import models

# Create your models here.
class ModeloViveros(models.Model):
    codigoVivero = models.CharField(max_length=10)
    nombreVivero = models.CharField(max_length=50)
    departamento = models.CharField(max_length=30)