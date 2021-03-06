# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User , Group


# Create your models here.

class estado_empresa(models.Model):
    estado_nombre_empresa = models.CharField(blank=True, max_length=100, verbose_name='Nombre')

    class Meta():
        verbose_name = "estado_empresa"
        verbose_name_plural = "estado_empresas"

    def __str__(self):
        return self.estado_nombre_empresa

class empresa(models.Model):
    nit_empresa = models.IntegerField(null=True, unique=True, verbose_name='NIT', max_length=11)
    nombre_empresa = models.CharField(blank=True, max_length=100, verbose_name='Nombre')
    estado_empresa = models.ForeignKey(estado_empresa, on_delete=models.CASCADE, null=True)
    usuarios = models.ManyToManyField(User)

    class Meta():
        verbose_name = "empresa"
        verbose_name_plural = "empresas"

    def __str__(self):
        return self.nombre_empresa

class campana_publicitaria(models.Model):
    nombre_campana = models.CharField(blank=True, max_length=100, verbose_name='Nombre')
    descripcion_campana = models.CharField(blank=True, max_length=100, verbose_name='Descripcion')
    objetivo_campana = models.CharField(blank=True, max_length=100, verbose_name='Objetivo')
    publico_campana = models.CharField(blank=True, max_length=100, verbose_name='Publico')
    ubicacion_campana = models.CharField(blank=True, max_length=100, verbose_name='Ubicacion')
    presupuesto_campana = models.IntegerField(null=True, verbose_name='Presupuesto')
    eficacia_camapana = models.CharField(blank=True, max_length=100, verbose_name='Eficacia')
    empresa_campana = models.ForeignKey(empresa, on_delete=models.CASCADE, null=True)
    usuario_campana = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta():
        verbose_name = "campana_publicitaria"
        verbose_name_plural = "campanas_publicitarias"

    def __str__(self):
        return self.nombre_campana

    
class ubicacion(models.Model):
    nombre_ubicacion = models.CharField(blank=True, max_length=100, verbose_name='Nombre')    

    class Meta():
        verbose_name = "ubicacion"
        verbose_name_plural = "ubicaciones"

    def __str__(self):
        return self.nombre_ubicacion

class hashtag(models.Model):
    nombre_hastag = models.CharField(blank=True, max_length=100, verbose_name='Nombre')
    

    class Meta():
        verbose_name = "hashtag"
        verbose_name_plural = "hashtags"

    def __str__(self):
        return self.nombre_hastag

class red_social(models.Model):
    nombre_red_social = models.CharField(blank=True, max_length=100, verbose_name='Nombre')
    usuario_red_social = models.CharField(blank=True, max_length=100, verbose_name='Usuario')
    fecha_inicio_red_social = models.DateField(auto_now=False, auto_now_add=False,verbose_name='Fecha de Inicio')
    fecha_final_red_social = models.DateField(auto_now=False, auto_now_add=False,verbose_name='Fecha Final')
    cantidad_seguidores_red_social = models.IntegerField(null=True, verbose_name='Cantidad de seguidores')
    cantidad_likes_red_social = models.IntegerField(null=True, verbose_name='Cantidad de Likes')
    cantidad_reacciones_red_social = models.IntegerField(null=True, verbose_name='Cantidad de reacciones')
    empresa_red_social = models.ForeignKey(empresa, on_delete=models.CASCADE, null=True)
    campana_publicitaria_red_social = models.ForeignKey(campana_publicitaria, on_delete=models.CASCADE, null=True)
    ubicacion_red_social = models.ForeignKey(ubicacion, on_delete=models.CASCADE, null=True)
    hashtag_red_social = models.ForeignKey(hashtag, on_delete=models.CASCADE, null=True)

    class Meta():
        verbose_name = "red_social"
        verbose_name_plural = "redes_sociales"

    def __str__(self):
        return self.nombre_red_social