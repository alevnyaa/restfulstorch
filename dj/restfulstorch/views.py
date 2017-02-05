from .models import Category, Store
from rest_framework import viewsets
from .serializers import CategorySerializer, StoreSerializer


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
