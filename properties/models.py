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
    TYPE_TRANSACTION = (
            (1, 'Venta'),
            (2, 'Renta')
            )
    address = models.ForeignKey('Address', related_name='properties', verbose_name='Dirección')
    price = models.FloatField('Precio en MXN', blank=True)
    number_of_rooms = models.IntegerField('Número de recámaras', blank=True)
    number_of_bathrooms = models.IntegerField('Número de baños', blank=True)
    area = models.IntegerField('Área en metros cuadrados', blank=True)
    url = models.URLField('URL de la publicación', max_length=300, blank=True)
    transaction_type = models.PositiveSmallIntegerField(
            'Tipo de transacción', choices=TYPE_TRANSACTION, default=1)
    score = models.FloatField('Puntuación')

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.address.street


class SalePropertyManager(models.Manager):
    def get_queryset(self):
        return super(SalePropertyManager, self).get_queryset().filter(
                transaction_type=1)


class RentPropertyManager(models.Manager):
    def get_queryset(self):
        return super(RentPropertyManager, self).get_queryset().filter(
                transaction_type=2)


class SaleProperty(Property):
    objects = SalePropertyManager()
    class Meta:
        proxy = True
        verbose_name = 'Inmueble en venta'
        verbose_name_plural = 'Inmuebles en venta'


class RentProperty(Property):
    objects = RentPropertyManager()
    class Meta:
        proxy = True
        verbose_name = 'Inmueble en renta'
        verbose_name_plural = 'Inmuebles en renta'
