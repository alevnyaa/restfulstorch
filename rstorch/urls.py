from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = 'rstorch'

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^categories/$', views.CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^stores/$', views.StoreList.as_view()),
    url(r'^stores/(?P<pk>[0-9]+)/$', views.StoreDetail.as_view()),
    url(r'^stores/(?P<latitude>[0-9]{2}\.[0-9]{6})/(?P<longitude>[0-9]{2}\.[0-9]{6})/(?P<query>[\w\-\\\.\']{2,50})/[a-z]{5}/$', views.StoreSearch.as_view()),
    url(r'^stores/(?P<latitude>[0-9]{2}\.[0-9]{6})/(?P<longitude>[0-9]{2}\.[0-9]{6})/(?P<query>[\w\-\\\.\']{2,50})/[a-z]{5}/?P<distance>[0-9]{1,5}/$', views.StoreSearch.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 ]
