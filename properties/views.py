from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from properties.models import Address, SaleProperty, RentProperty


class SalePropertyListView(ListView):
    model = SaleProperty


class SalePropertyDetailView(DetailView):
    model = SaleProperty
    http_method_names = ['get']


class RentPropertyListView(ListView):
    model = RentProperty


class RentPropertyDetailView(DetailView):
    model = RentProperty
    http_method_names = ['get']
    template_name = 'rent-detail-prperty.html'

