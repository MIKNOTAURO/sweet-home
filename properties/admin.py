from django.contrib import admin

from properties.models import Address, SaleProperty, RentProperty

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(SaleProperty)
class SalePropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(RentProperty)
class RentPropertyAdmin(admin.ModelAdmin):
    pass
