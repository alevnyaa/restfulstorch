from .models import Category, Place
from rest_framework import viewsets
from .serializers import CategorySerializer, PlaceSerializer, PlaceDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceDetailSerializer


