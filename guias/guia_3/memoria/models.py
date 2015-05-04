from django.db import models


class Perfil(models.Model):
    nickname = models.CharField(max_length=25)

class Dificultad(models.Model):
    nombre = models.CharField(max_length=15)
    largo = models.IntegerField()

class Puntaje(models.Model):
    perfil = models.ForeignKey(Perfil)
    dificultad = models.ForeignKey(Dificultad)
    puntuacion = models.FloatField()