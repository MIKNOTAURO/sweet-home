from django.contrib import admin

from properties.models import Address, Property

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass
