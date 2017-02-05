from django.contrib import admin

from .models import Category, Store

class CategoryAdmin(admin.ModelAdmin):
    pass

class StoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
