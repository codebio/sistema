# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora', models.IntegerField()),
                ('votos', models.IntegerField()),
                ('cola', models.CharField(max_length=1, choices=[(b'F', b'FULL'), (b'C', b'CON COLA'), (b'V', b'VACIO')])),
                ('incidencia', models.CharField(max_length=1, choices=[(b'S', b'SERVICIOS'), (b'L', b'LOGISTICA'), (b'C', b'CNE'), (b'O', b'ORDEN PUBLICO')])),
                ('detalle', models.CharField(max_length=300)),
                ('nombre', models.ForeignKey(related_name='Reporte_del_centro', to='principal.Nucleado')),
            ],
        ),
    ]
