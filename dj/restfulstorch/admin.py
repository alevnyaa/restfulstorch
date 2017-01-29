from django.contrib import admin

from .models import Category, Company

class CategoryAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
