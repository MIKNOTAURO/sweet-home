# -*- coding: utf-8 -*-
from django.db import models


class Address(models.Model):
    street = models.CharField('Calle', max_length=100)
    street_number = models.CharField('Número exterior', max_length=10, blank=True)
    neighborhood = models.CharField('Colonia', max_length=100, blank=True)
    zip_code = models.PositiveSmallIntegerField('Código postal')
    town = models.CharField('Delegación/Municipio', max_length=100, blank=True)
    lat = models.FloatField('Latitud', blank=True)
    lng = models.FloatField('Longitud', blank=True)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return self.street


class Property(models.Model):
    address = models.ForeignKey('Address', related_name='properties', verbose_name='Dirección')
    price = models.FloatField('Precio en MXN', blank=True)
    number_of_rooms = models.IntegerField('Número de recámaras', blank=True)
    number_of_bathrooms = models.IntegerField('Número de baños', blank=True)
    area = models.IntegerField('Área en metros cuadrados', blank=True)
    score = models.FloatField('Puntuación')

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.address.street
