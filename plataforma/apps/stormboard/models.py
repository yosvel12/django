from django.db import models

# Create your models here.

class Prueba(models.Model):
    name = models.CharField(max_length=255)
