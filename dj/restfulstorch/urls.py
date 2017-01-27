from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = 'restfulstorch'

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet, 'categories')
router.register(r'places', views.PlaceViewSet, 'places')
router.register(r'placedetail', views.PlaceDetailViewSet, 'placedetail')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls, namespace='rest_framework')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
