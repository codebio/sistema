# -*- encoding: utf-8 -*-
from django.db import models
from principal.models import Nucleado, Circunscripcion

# Create your models here.
#encoding:utf-8
#-*- coding: utf-8 -*-
class Centro(models.Model):
	"""Participacion en Centros nucleados"""
	hora = models.IntegerField()
	nombre = models.ForeignKey(Nucleado, related_name='Reporte_del_centro')
	votos = models.IntegerField()
	COLA_SELECCION=(
		('FULL','FULL'),
		('CON COLA','CON COLA'),
		('VACIO','VACIO'),
	)
	cola = models.CharField(max_length=8, choices=COLA_SELECCION)
	INCIDENCIA_SELECCION=(
		('SERVICIOS','SERVICIOS'),
		('LOGISTICA','LOGISTICA'),
		('CNE','CNE'),
		('ORDEN PUBLICO','ORDEN PUBLICO'),
		('VARIOS','VARIOS'),
	)
	incidencia = models.CharField(max_length=13, choices=INCIDENCIA_SELECCION)
	detalle = models.CharField(max_length=300)
	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return str(self.nombre).encode("utf-8")

class Resultados(models.Model):
	"""Resultados por mesa por candidato"""
	circuito = models.ForeignKey(Circunscripcion, related_name='Circuito_resultados')
	centro = models.ForeignKey(Nucleado, related_name='centro_resultados')
	NUMERO_MESAS=(
		('1','Mesa 1'),
		('2','Mesa 2'),
		('3','Mesa 3'),
		('4','Mesa 4'),
	)
	mesa = models.CharField(max_length=1, choices=NUMERO_MESAS)
	postulado1 = models.IntegerField()
	postulado2 = models.IntegerField()
	postulado3 = models.IntegerField()
	postulado4 = models.IntegerField()
	postulado5 = models.IntegerField()
	postulado6 = models.IntegerField()
	postulado7 = models.IntegerField()
	postulado8 = models.IntegerField()
	postulado9 = models.IntegerField()
	postulado10 = models.IntegerField()
	postulado11 = models.IntegerField()
	postulado12 = models.IntegerField()
	observacion = models.CharField(max_length=300)
	def __str__(self):
		return self.centro

	def __unicode__(self):
		return str(self.centro).encode("utf-8")