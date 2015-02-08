from django.conf.urls import url, patterns
from accesorios import views

urlpatterns = patterns('',
		url(r'^lista/$', views.lista, name='lista'),
		url(r'^lista/correas/$', views.lista_correas, name='lista_correas'),
		url(r'^lista/pecheras/$', views.lista_pecheras, name='lista_pecheras'),
		url(r'^lista/collares/$', views.lista_collares, name='lista_collares'),
		url(r'^lista/chalecos/$', views.lista_chalecos, name='lista_chalecos'),
	)