from django.db import models
from django_mysql.models import ListCharField


# Create your models here.

class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    tipos = ListCharField(
        base_field=models.CharField(max_length=100)
    )
    peso = models.FloatField()
    altura = models.FloatField()
    descricao = models.TextField()


