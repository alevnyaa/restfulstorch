from .models import Category, Store, StoreDetails, BusinessHours
from rest_framework import viewsets
from .serializers import CategorySerializer, StoreSerializer, StoreDetailsSerializer, BusinessHoursSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = StoreDetails.objects.all()
    serializer_class = StoreDetailsSerializer


class BusinessHoursViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BusinessHours.objects.all()
    serializer_class = BusinessHoursSerializer
