from django.db import models
from django.contrib.auth.models import User
from orgs.models import OSC


class Tag(models.Model):
    tagId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()


class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    favoritos = models.ManyToManyField(OSC, blank=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return self.usuario.username
