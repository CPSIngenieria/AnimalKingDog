from django.shortcuts import render, get_object_or_404
from juguetes.models import Pelota

def lista(request):
	pelotas = Pelota.objects.all().order_by('-fecha_creacion')
	context = {
		'pelotas':pelotas,
	}
	return render(request, 'juguetes/lista_juguetes.html', context)

def lista_pelotas(request):
	pelotas = Pelota.objects.all().order_by('-fecha_creacion')
	context = {
		'pelotas':pelotas,
	}
	return render(request, 'juguetes/lista_pelotas.html', context)

def detalle_pelota(request, id_pelota):
	pelota = get_object_or_404(Pelota,pk=id_pelota)
	pelota.precio = '$ {:,}'.format(pelota.precio)
	context = {
		'pelota':pelota,
	}
	return render(request, 'juguetes/detalle_pelota.html', context)