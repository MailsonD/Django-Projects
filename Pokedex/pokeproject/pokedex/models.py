from django.db import models
from django_mysql.models import ListCharField


# Create your models here.

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    tipos = ListCharField(
        base_field=models.CharField(max_length=100),
        max_length=50
    )
    altura = models.FloatField()
    peso = models.FloatField()
    descricao = models.TextField()


