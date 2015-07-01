# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
                ('apertura', models.CharField(max_length=8)),
                ('cierre', models.CharField(max_length=8)),
                ('incidencia', models.CharField(max_length=1, choices=[(b'S', b'SERVICIOS'), (b'L', b'LOGISTICA'), (b'C', b'CNE'), (b'O', b'ORDEN PUBLICO')])),
                ('detalle', models.CharField(max_length=300)),
                ('nucleo', models.ForeignKey(related_name='Mesas', to='principal.Nucleado')),
            ],
        ),
    ]
