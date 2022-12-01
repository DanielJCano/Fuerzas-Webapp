from django.db import models
import socket
import select
import sys
from _thread import *
# Create your models here.

class Colector_datos(models.Model):
    fecha = models.DateField(null=True)
    tiempo = models.IntegerField()
    dato = models.IntegerField()