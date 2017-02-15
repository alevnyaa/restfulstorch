from django.contrib import admin

from .models import Category, Store, StoreDetails, BusinessHours

class CategoryAdmin(admin.ModelAdmin):
    pass

class StoreAdmin(admin.ModelAdmin):
    fields = (('store_code', 'store_name'), 'latitude')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(StoreDetails)
admin.site.register(BusinessHours)
