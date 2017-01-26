from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = 'restfulstorch'

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'placedetail', views.PlaceDetailViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
