# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centro',
            name='cola',
            field=models.CharField(max_length=8, choices=[(b'FULL', b'FULL'), (b'CON COLA', b'CON COLA'), (b'VACIO', b'VACIO')]),
        ),
        migrations.AlterField(
            model_name='centro',
            name='incidencia',
            field=models.CharField(max_length=13, choices=[(b'SERVICIOS', b'SERVICIOS'), (b'LOGISTICA', b'LOGISTICA'), (b'CNE', b'CNE'), (b'ORDEN PUBLICO', b'ORDEN PUBLICO'), (b'VARIOS', b'VARIOS')]),
        ),
    ]
