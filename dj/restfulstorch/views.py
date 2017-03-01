from .models import Category, Store
from rest_framework import viewsets
from .serializers import CategorySerializer, StoreSerializer
#from restfulstorch.permissions import IsAdminOrIsSelf
from rest_framework.decorators import list_route

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
    #permission_classes=[IsAdminOrIsSelf], `
    #@list_route(methods=['get'], url_path='^search/{latitude}/{longitude}/{distance}/$')
    #def searchByLocationWithDistance(self, request, latitude=None, longitude=None, distance=None):
    #    queryset = Store.objects.all()
    #    serializer = UserSerializer(queryset, many=True)
    #    return Response(serializer.data)
