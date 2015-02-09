from django.conf.urls import url, patterns
from accesorios import views

urlpatterns = patterns('',
		url(r'^lista/$', views.lista, name='lista'),
		url(r'^lista/correas/$', views.lista_correas, name='lista_correas'),
		url(r'^lista/pecheras/$', views.lista_pecheras, name='lista_pecheras'),
		url(r'^lista/collares/$', views.lista_collares, name='lista_collares'),
		url(r'^lista/chalecos/$', views.lista_chalecos, name='lista_chalecos'),
		url(r'^detalle/correas/(?P<id_correa>[\d]+)/$', views.detalle_correa, name='detalle_correa'),
		url(r'^detalle/pecheras/(?P<id_pechera>[\d]+)/$', views.detalle_pechera, name='detalle_pechera'),
		url(r'^detalle/collares/(?P<id_collar>[\d]+)/$', views.detalle_collar, name='detalle_collar'),
		url(r'^detalle/chalecos/(?P<id_chaleco>[\d]+)/$', views.detalle_chaleco, name='detalle_chaleco'),
	)