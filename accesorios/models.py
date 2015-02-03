from django.db import models

class Correa(models.Model):
	nombre = models.CharField( max_length=70 )
	precio = models.PositiveIntegerField( default=0 )
	descripcion = models.TextField()
	boton_comprar = models.TextField()

	def __unicode__(self):
		return self.nombre