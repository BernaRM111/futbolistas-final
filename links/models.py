from django.db import models


class Link(models.Model):
    nombre = models.TextField()
    edad = models.IntegerField()
    nacionalidad = models.TextField(blank=True)
    estatura = models.IntegerField()
    peso = models.IntegerField()
    club = models.TextField(blank=True)
    posicion = models.TextField(blank=True)
    goles = models.IntegerField()
    asistencias = models.IntegerField()
    imagen = models.TextField(blank=True)
