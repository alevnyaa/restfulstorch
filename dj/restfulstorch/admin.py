from django.contrib import admin

from .models import Category, Store

class CategoryAdmin(admin.ModelAdmin):
    fields = (('name_tr', 'name_en'), 'parent', 'stores')

class StoreAdmin(admin.ModelAdmin):
    fields = (
            'store_code',
            'store_name',
            ('latitude', 'longitude'),
            'address',
            'primary_phone_number',
            'secondary_phone_number',
            'email_address',
            'website_address',
            'contact_name',
            'contact_phone_number',
            'contact_email_address',
            ('hours_monday_open', 'hours_monday_close'),
            ('hours_tuesday_open', 'hours_tuesday_close'),
            ('hours_wednesday_open', 'hours_wednesday_close'),
            ('hours_thursday_open', 'hours_thursday_close'),
            ('hours_friday_open', 'hours_friday_close'),
            ('hours_saturday_open', 'hours_saturday_close'),
            ('hours_sunday_open', 'hours_sunday_close')
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
