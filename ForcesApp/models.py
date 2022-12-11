from django.db import models
import socket
import select
import sys
from _thread import *
# Create your models here.

class Colector_datos(models.Model):
    fecha = models.CharField(max_length=100, null=True)
    tiempo = models.FloatField()
    dato = models.FloatField()