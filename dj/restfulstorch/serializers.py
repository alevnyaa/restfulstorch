from .models import Category, Company
from rest_framework import serializers

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('store_name', 'address', 'latitude', 'longitude')

class CompanyDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('store_name', 'address', 'latitude', 'longitude', 'email_address', 'website_address', 'primary_phone_number', 'secondary_phone_number')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    companies = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name_tr', 'name_en', 'parent_cat', 'companies')

