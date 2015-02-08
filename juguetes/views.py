from django.shortcuts import render

def lista(request):
	return render(request, 'juguetes/lista_juguetes.html')

def lista_pelotas(request):
	return render(request, 'juguetes/lista_pelotas.html')