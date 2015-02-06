from django.db import models

class Pelota(models.Model):
	nombre = models.CharField( max_length=70 )
	precio = models.PositiveIntegerField( default=0 )
	descripcion = models.TextField()
	boton_comprar = models.TextField()
	foto = models.ImageField(upload_to='fotos_pelotas')

	def __unicode__(self):
		return self.nombre

	def boton_admin(self):
		return self.boton_comprar
	boton_admin.allow_tags = True

	def foto_admin(self):
		return "<img src='%s' width='100'></img>" % self.foto.url
	foto_admin.allow_tags = True