from django.db import models


# Create your models here.
class item(models.Model):
    nombre = models.CharField(max_length=200)