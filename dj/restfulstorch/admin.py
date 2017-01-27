from django.contrib import admin

from .models import Category, Place

class CategoryAdmin(admin.ModelAdmin):
    pass

class PlaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Place, PlaceAdmin)
