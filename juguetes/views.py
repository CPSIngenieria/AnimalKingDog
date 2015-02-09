from django.shortcuts import render
from juguetes.models import Pelota

def lista(request):
	return render(request, 'juguetes/lista_juguetes.html')

def lista_pelotas(request):
	pelotas = Pelota.objects.all().order_by('-fecha_creacion')
	context = {
		'pelotas':pelotas,
	}
	return render(request, 'juguetes/lista_pelotas.html', context)