from django.contrib import admin
from accesorios.models import Correa, Pechera, Collar, Chaleco

class CorreaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio', 'descripcion', 'boton_admin', 'foto_admin')
	search_fields = ['nombre', 'descripcion']

class PecheraAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio', 'descripcion', 'boton_admin', 'foto_admin')
	search_fields = ['nombre', 'descripcion']

class CollarAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio', 'descripcion', 'boton_admin', 'foto_admin')
	search_fields = ['nombre', 'descripcion']

class ChalecoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'precio', 'descripcion', 'boton_admin', 'foto_admin')
	search_fields = ['nombre', 'descripcion']

admin.site.register(Correa, CorreaAdmin)
admin.site.register(Pechera, PecheraAdmin)
admin.site.register(Collar, CollarAdmin)
admin.site.register(Chaleco, ChalecoAdmin)
