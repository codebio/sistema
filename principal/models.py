# -*- encoding: utf-8 -*-
from django.db import models
# Create your models here.
#encoding:utf-8
#-*- coding: utf-8 -*-
class Circunscripcion(models.Model):
	"""Circuitos electorales"""
	numero = models.IntegerField()
	poblacion = models.IntegerField(blank=True)
	rep = models.IntegerField(blank=True)
	delegados = models.IntegerField(blank=True)
	clp = models.IntegerField(blank=True)
	ubch =models.IntegerField(blank=True)
	patrullas =models.IntegerField(blank=True)
	
	def __str__(self):
		return self.numero

	def __unicode__(self):
		return str(self.numero)

class Nucleado(models.Model):
	"""Centros nucleados"""
	nombre = models.CharField(max_length=100,)
	circuito = models.ForeignKey(Circunscripcion, related_name='Nucleos')
	municipio = models.CharField(max_length=100)
	parroquia = models.CharField(max_length=100)
	mesas = models.IntegerField()

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return str(self.nombre).encode("utf-8")

class Centroe(models.Model):
	"""Centros electorales"""
	nombre = models.CharField(max_length=100,)
	nucleo = models.ForeignKey(Nucleado, related_name='Centros')
	jefe = models.CharField(max_length=100)
	cedula = models.CharField(max_length=100)
	telefono = models.IntegerField()

	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return str(self.nombre).encode("utf-8")

class Mesa(models.Model):
	"""Mesas electorales"""
	nucleo = models.ForeignKey(Nucleado, related_name='Mesas')
	NUMERO_MESAS=(
		('1','Mesa 1'),
		('2','Mesa 2'),
		('3','Mesa 3'),
		('4','Mesa 4'),
	)
	numero = models.CharField(max_length=1, choices=NUMERO_MESAS)
	apertura = models.CharField(max_length=8)
	cierre = models.CharField(max_length=8)
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

class Postulado(models.Model):
	"""Candidatos PSUV"""
	circuito = models.ForeignKey(Circunscripcion, related_name='Circuito_candidato')
	CODIGO_SELECCION=(
		('MM','MUJER MAYOR'),
		('HM','HOBRE MAYOR'),
		('MJ','MUJER JOVEN'),
		('HJ','HOMBRE JOVEN'),
	)
	codigo = models.CharField(max_length=12, choices=CODIGO_SELECCION)
	nombre = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre

	def __unicode__(self):
		return str(self.nombre).encode("utf-8")