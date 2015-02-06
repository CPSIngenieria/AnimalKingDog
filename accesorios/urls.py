from django.conf.urls import url, patterns
from accesorios import views

urlpatterns = patterns('',
		url(r'^lista/$', views.lista, name='lista'),
	)