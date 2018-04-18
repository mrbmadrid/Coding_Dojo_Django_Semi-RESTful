from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^users$', views.index),
	url(r'^users/(?P<id>\d+)$', views.show),
	url(r'^users/(?P<id>\d+)/edit$', views.edit),
	url(r'^users/(?P<id>\d+)/delete$', views.delete),
	url(r'^users/add$', views.add)
]