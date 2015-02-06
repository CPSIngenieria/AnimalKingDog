from django.shortcuts import render

def lista(request):
	return render(request, 'accesorios/accesorios_lista.html')