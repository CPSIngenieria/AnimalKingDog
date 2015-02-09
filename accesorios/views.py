from django.shortcuts import render
from accesorios.models import Correa, Chaleco, Pechera, Collar


def lista(request):
	return render(request, 'accesorios/lista_accesorios.html')

def lista_correas(request):
	correas = Correa.objects.all().order_by('-fecha_creacion')
	context = {
		'correas':correas,
	}
	return render(request, 'accesorios/lista_correas.html', context)

def lista_pecheras(request):
	pecheras = Pechera.objects.all().order_by('-fecha_creacion')
	context = {
		'pecheras':pecheras
	}
	return render(request, 'accesorios/lista_pecheras.html', context)

def lista_collares(request):
	collares = Collar.objects.all().order_by('-fecha_creacion')
	context = {
		'collares':collares,
	}
	return render(request, 'accesorios/lista_collares.html', context)

def lista_chalecos(request):
	chalecos = Chaleco.objects.all().order_by('-fecha_creacion')
	context = {
		'chalecos':chalecos,
	}
	return render(request, 'accesorios/lista_chalecos.html', context)