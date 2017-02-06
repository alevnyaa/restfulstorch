from .models import Category, Store, StoreDetails, BusinessHours
from rest_framework import serializers

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    stores = StoreSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'

class StoreDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoreDetails
        fields = '__all__'

class BusinessHoursSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessHours
        fields = '__all__'

