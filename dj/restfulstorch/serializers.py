from .models import Category, Store, StoreDetails, BusinessHours
from rest_framework import serializers

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    stores = StoreSerializer(many=True)

    def get_parent(self, obj):
        if obj.parent is not None:
            return CategorySerializer(obj.parent).data
        else:
            return None

    class Meta:
        model = Category
        fields = ('name_tr', 'name_en', 'id', 'parent', 'stores')

class StoreDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoreDetails
        fields = '__all__'

class BusinessHoursSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessHours
        fields = '__all__'

