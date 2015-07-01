# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_postulado'),
        ('participacion', '0002_auto_20150628_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mesa', models.CharField(max_length=1, choices=[(b'1', b'Mesa 1'), (b'2', b'Mesa 2'), (b'3', b'Mesa 3'), (b'4', b'Mesa 4')])),
                ('postulado1', models.IntegerField()),
                ('observacion', models.CharField(max_length=300)),
                ('centro', models.ForeignKey(related_name='centro_resultados', to='principal.Nucleado')),
                ('circuito', models.ForeignKey(related_name='Circuito_resultados', to='principal.Circunscripcion')),
            ],
        ),
    ]
