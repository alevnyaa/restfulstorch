from .models import Category, Store
from rest_framework import serializers

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = ('store_name', 'address', 'latitude', 'longitude', 'email_address', 'website_address', 'primary_phone_number', 'secondary_phone_number')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    companies = StoreSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name_tr', 'name_en', 'parent_cat', 'companies')

