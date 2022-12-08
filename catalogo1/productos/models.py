from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()


    def __str__(self):
        return self.nombre