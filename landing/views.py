from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def home(request):
	return render(request, 'landing/landing.html')

def contactar(request):
	return HttpResponseRedirect(reverse('landing:home'))