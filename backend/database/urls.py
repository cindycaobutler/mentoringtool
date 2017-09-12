from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<table>\w+)/(?P<id>\d+)$', views.parseRequest, name='parseRequest'),
    url(r'^(?P<table>\w+)/(?P<id>\d+)/insert$', views.insertData, name='insertData'),
    url(r'^(?P<table>\w+)/(?P<id>\d+)/update$', views.updateData, name='updateData'),
    url(r'^(?P<table>\w+)/(?P<id>\d+)/delete$', views.deleteData, name='deleteData')
]