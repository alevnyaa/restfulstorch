from .models import Category, Place
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name_tr', 'name_en')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('store_name', 'address', 'latitude', 'longitude')

class PlaceDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('store_name', 'address', 'latitude', 'longitude', 'email_address', 'website_address', 'primary_phone_number', 'secondary_phone_number')
