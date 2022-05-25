from django.db import models

# Create your models here.
class Producto(models.Model):
    nombreProducto= models.CharField(max_length=10)
    FrecuenAplicacion= models.CharField(max_length=50)
    ValorProcducto = models.CharField(max_length=30)
    