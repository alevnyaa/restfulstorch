from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = 'restfulstorch'

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet, 'categories')
router.register(r'stores', views.StoreViewSet, 'stores')
router.register(r'storedetails', views.StoreDetailsViewSet, 'storedetails')
router.register(r'businesshours', views.BusinessHoursViewSet, 'businesshours')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls, namespace='rest_framework')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
