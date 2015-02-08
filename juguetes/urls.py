from django.conf.urls import url, patterns
from juguetes import views

urlpatterns = patterns('',
	url(r'^lista/$', views.lista, name='lista'),
	url(r'^lista/pelotas$', views.lista_pelotas, name='lista_pelotas'),
)