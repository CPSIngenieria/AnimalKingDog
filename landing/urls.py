from django.conf.urls import url, patterns
from landing import views

urlpatterns = patterns('',
		url(r'^$', views.home, name='home'),
		url(r'^contacto/$', views.contacto, name='contacto'),
		url(r'^contactar/$', views.contactar, name='contactar')
	)