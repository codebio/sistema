# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20150628_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=12, choices=[(b'MM', b'MUJER MAYOR'), (b'HM', b'HOBRE MAYOR'), (b'MJ', b'MUJER JOVEN'), (b'HJ', b'HOMBRE JOVEN')])),
                ('nombre', models.CharField(max_length=100)),
                ('circuito', models.ForeignKey(related_name='Circuito_candidato', to='principal.Circunscripcion')),
            ],
        ),
    ]
