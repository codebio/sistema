# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centroe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('jefe', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Circunscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('poblacion', models.IntegerField(blank=True)),
                ('rep', models.IntegerField(blank=True)),
                ('delegados', models.IntegerField(blank=True)),
                ('clp', models.IntegerField(blank=True)),
                ('ubch', models.IntegerField(blank=True)),
                ('patrullas', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nucleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('parroquia', models.CharField(max_length=100)),
                ('mesas', models.IntegerField()),
                ('circuito', models.ForeignKey(related_name='Nucleos', to='principal.Circunscripcion')),
            ],
        ),
        migrations.AddField(
            model_name='centroe',
            name='nucleo',
            field=models.ForeignKey(related_name='Centros', to='principal.Nucleado'),
        ),
    ]
