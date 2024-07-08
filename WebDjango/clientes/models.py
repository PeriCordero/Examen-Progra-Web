from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_dibujo = models.CharField(max_length=100)
    correo = models.EmailField()
    instagram = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
