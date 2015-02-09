from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from accesorios.models import Correa, Chaleco, Pechera, Collar
from juguetes.models import Pelota

def home(request):
	correas = Correa.objects.order_by('-fecha_creacion')[:4]
	pecheras = Pechera.objects.order_by('-fecha_creacion')[:4]
	chalecos = Chaleco.objects.order_by('-fecha_creacion')[:4]
	collares = Collar.objects.order_by('-fecha_creacion')[:4]
	context = {
		'correas':correas,
		'pecheras':pecheras,
		'chalecos':chalecos,
		'collares':collares,
	}
	return render(request, 'landing/landing.html', context)

def contactar(request):
	return HttpResponseRedirect(reverse('landing:home'))