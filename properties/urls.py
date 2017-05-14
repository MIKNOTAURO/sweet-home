from django.conf.urls import url

from properties.views import SalePropertyListView, RentPropertyListView

urlpatterns = [
    url(r'^venta/$', SalePropertyListView.as_view(), name='sale-property-list-view'),
    url(r'^renta/$', RentPropertyListView.as_view(), name='rent-property-list-view'),
]
