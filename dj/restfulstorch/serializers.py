from .models import Category, Store, StoreDetails, BusinessHours
from rest_framework import serializers

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    str_en = serializers.SerializerMethodField()
    str_tr = serializers.SerializerMethodField()
    stores = StoreSerializer(many=True)

    #parent = serializers.SerializerMethodField()
    #def get_parent(self, obj):
    #    if obj.parent is not None:
    #        return CategorySerializer(obj.parent).data
    #    else:
    #        return None

    def get_str_en(self, obj):
        return obj.__str__()

    def get_str_tr(self, obj):
        return obj.str_tr()

    class Meta:
        model = Category
        fields = ('id', 'str_en', 'str_tr', 'name_en', 'name_tr', 'parent', 'stores')

class StoreDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StoreDetails
        fields = '__all__'

class BusinessHoursSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BusinessHours
        fields = '__all__'

