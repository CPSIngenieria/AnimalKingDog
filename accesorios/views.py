from django.shortcuts import render

def lista(request):
	return render(request, 'accesorios/lista_accesorios.html')

def lista_correas(request):
	return render(request, 'accesorios/lista_correas.html')

def lista_pecheras(request):
	return render(request, 'accesorios/lista_pecheras.html')

def lista_collares(request):
	return render(request, 'accesorios/lista_collares.html')

def lista_chalecos(request):
	return render(request, 'accesorios/lista_chalecos.html')