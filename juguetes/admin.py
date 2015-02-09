from django.contrib import admin
from juguetes.models import Pelota

class PelotaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio', 'descripcion', 'fecha_creacion','boton_admin', 'foto_admin')
	search_fields = ['nombre','descripcion']

admin.site.register(Pelota, PelotaAdmin)
