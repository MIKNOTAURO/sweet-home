from django.conf.urls import url

from properties.views import (
        SalePropertyListView, 
        RentPropertyListView, 
        SalePropertyDetailView, 
        RentPropertyDetailView
    )

urlpatterns = [
    url(r'^venta/$', SalePropertyListView.as_view(), name='sale-property-list-view'),
    url(r'^renta/$', RentPropertyListView.as_view(), name='rent-property-list-view'),
    url(r'^venta/(?P<pk>\d+)/$', SalePropertyDetailView.as_view(), name='sale-property-detail-view'),
    url(r'^renta/(?P<pk>\d+)/$', RentPropertyDetailView.as_view(), name='rent-property-detail-view'),
]
