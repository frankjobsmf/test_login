from django.db import models

class Aparcamiento(models.Model):
    direccion = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return self.direccion
    
