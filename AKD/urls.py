from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings 

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'AKD.views.home', name='home'),
    url(r'^', include('landing.urls', namespace='landing')),
    url(r'^accesorios/', include('accesorios.urls', namespace='accesorios')),
    url(r'^juguetes/', include('juguetes.urls', namespace='juguetes')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	)