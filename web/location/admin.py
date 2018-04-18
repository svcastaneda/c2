from django.contrib import admin

from address.forms import AddressWidget
from address.models import AddressField

from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    '''Admin View for Location'''

    list_display = (
        'address',
        'location_type',
    )

    list_filter = (
        'location_type',
    )

    search_fields = (
        'address',
        'location_type',
    )

    fieldsets = (
        (
            "",
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'address',
                    'location_type',
                )
            }
        ),
    )

    formfield_overrides = {
        AddressField: {
            'widget': AddressWidget(
                attrs={
                    'style': 'width: 400px;'
                }
            )
        }
    }
