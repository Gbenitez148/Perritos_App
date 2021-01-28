from django.db import models


# Create your models here.
class Carrousel(models.Model):
    #biblio: https://tutorial.djangogirls.org/es/django_models/
    #       https://docs.djangoproject.com/en/3.1/topics/db/models/
    #CAMPO = models.ForeignKey(MODELO, on_delete=models.CASCADE)
    #CAMPO = models.TextField(null=True, blank=True)
    #CAMPO = models.CharField(max_length=128, null=False, blank=True, 
    #                       default="sin informacion", choices=CAMPO_TIPO_DE_DATO)
    #CAMPO = models.IntegerField(null=True)
    #CAMPO = models.DateTimeField(null=True)
    #CAMPO = models.FileField(BUSCAR PARAMETROS)
    #Que datos debe tener carrousel?
    foto = models.ImageField(upload_to="Media") 
    titulo = models.CharField(max_length=64, null=False, default="sin titulo")
    texto = models.CharField(max_length=128, null=True)
    pie_de_pagina = models.CharField(max_length=128, null=True)
    habilitado = models.BooleanField()
    fh_creacion = models.DateTimeField(auto_now_add=True)
    fh_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
