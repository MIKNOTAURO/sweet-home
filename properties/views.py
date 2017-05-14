from django.shortcuts import render
from django.views.generic.list import ListView

from properties.models import Address, SaleProperty, RentProperty


class SalePropertyListView(ListView):
    model = SaleProperty


class RentPropertyListView(ListView):
    model = RentProperty
