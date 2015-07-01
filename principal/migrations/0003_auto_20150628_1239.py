# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_mesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='incidencia',
            field=models.CharField(max_length=13, choices=[(b'SERVICIOS', b'SERVICIOS'), (b'LOGISTICA', b'LOGISTICA'), (b'CNE', b'CNE'), (b'ORDEN PUBLICO', b'ORDEN PUBLICO'), (b'VARIOS', b'VARIOS')]),
        ),
    ]
