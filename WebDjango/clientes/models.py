from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.user.username

class Dibujo(models.Model):
    TIPO_CHOICES = [
        ('P', 'Pequeño'),
        ('M', 'Mediano'),
        ('G', 'Grande'),
    ]
    id_dibujo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre
    

