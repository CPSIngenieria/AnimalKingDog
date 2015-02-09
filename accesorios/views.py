from django.shortcuts import render, get_object_or_404
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

def detalle_correa(request, id_correa):
	correa = get_object_or_404(Correa,pk=id_correa)
	correa.precio = '$ {:,}'.format(correa.precio)
	context = {
		'correa':correa,
	}
	return render(request, 'accesorios/detalle_correa.html', context)

def detalle_pechera(request, id_pechera):
	pechera = get_object_or_404(Pechera,pk=id_pechera)
	pechera.precio = '$ {:,}'.format(pechera.precio)
	context = {
		'pechera':pechera,
	}
	return render(request, 'accesorios/detalle_pechera.html', context)

def detalle_collar(request, id_collar):
	collar = get_object_or_404(Collar,pk=id_collar)
	collar.precio = '$ {:,}'.format(collar.precio)
	context = {
		'collar':collar,
	}
	return render(request, 'accesorios/detalle_collar.html', context)

def detalle_chaleco(request, id_chaleco):
	chaleco = get_object_or_404(Chaleco,pk=id_chaleco)
	chaleco.precio = '$ {:,}'.format(chaleco.precio)
	context = {
		'chaleco':chaleco,
	}
	return render(request, 'accesorios/detalle_chaleco.html', context)