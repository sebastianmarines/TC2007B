from django.db import models


class Tag(models.Model):
    tagId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class OSC(models.Model):
    oscId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    alias = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    direccion = models.TextField()
    coordenadas_latitud = models.FloatField()
    coordenadas_longitud = models.FloatField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    areaContacto = models.CharField(max_length=255)
    horaAtencion = models.CharField(max_length=255)
    paginaWeb = models.URLField()
    redesSociales = models.JSONField()
    videos = models.ManyToManyField("Multimedia", related_name="osc_videos", blank=True)
    imagenes = models.ManyToManyField(
        "Multimedia", related_name="osc_imagenes", blank=True
    )
    articulosInteres = models.ManyToManyField(
        "Multimedia", related_name="osc_articulos", blank=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "OSC"
        verbose_name_plural = "OSCs"


class Multimedia(models.Model):
    url = models.URLField()
