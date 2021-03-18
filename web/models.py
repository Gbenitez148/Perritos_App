from django.db import models

#  traer de algun servidor externo, las razas de perro. Crome endjango que lo haga automatico  (como cel;ery) o algun servicio en linux


class Carrousel(models.Model):
    #  biblio: https://tutorial.djangogirls.org/es/django_models/
    #       https://docs.djangoproject.com/en/3.1/topics/db/models/
    #  CAMPO = models.ForeignKey(MODELO, on_delete=models.CASCADE)
    #  CAMPO = models.TextField(null=True, blank=True)
    #  CAMPO = models.CharField(max_length=128, null=False, blank=True, 
    #                       default="sin informacion", choices=CAMPO_TIPO_DE_DATO)
    #  CAMPO = models.IntegerField(null=True)
    #  CAMPO = models.DateTimeField(null=True)
    #  CAMPO = models.FileField(BUSCAR PARAMETROS)
    #  Que datos debe tener carrousel?
    foto = models.ImageField(upload_to="Media") 
    titulo = models.CharField(max_length=64, default="sin titulo")
    texto = models.CharField(max_length=128, null=True)
    pie_de_pagina = models.CharField(max_length=128, null=True)
    habilitado = models.BooleanField()
    fh_creacion = models.DateTimeField(auto_now_add=True)
    fh_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Perro(models.Model):
    nombre = models.CharField(max_length=64)
    raza = models.CharField(max_length=64)
    fh_nacimiento = models.DateTimeField()
    valor_venta = models.IntegerField(null=True)
    #  posibles campos
    #  dias #Esto se puede hacer con una funcion, que lo calcule automaticamente
    #  habilitado_venta #flag

    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=64)
    direccion = models.CharField(max_length=64)
    telefono = models.IntegerField(null=True)  # mejorar el numero de telefono
    mail = models.EmailField(max_length=254)
    mision = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre


class Entrega(models.Model):
    nombre = models.CharField(max_length=34)
    seña = models.IntegerField(null=True)
    vacunas = models.CharField(max_length=64)
    días_nacido = models.IntegerField(null=True)
