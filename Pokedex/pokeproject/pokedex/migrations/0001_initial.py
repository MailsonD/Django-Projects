# Generated by Django 2.2.5 on 2019-09-23 18:25

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('tipos', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=50, size=None)),
                ('altura', models.FloatField()),
                ('peso', models.FloatField()),
                ('descricao', models.TextField()),
            ],
        ),
    ]
