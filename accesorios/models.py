from django.db import models

class Correa(models.Model):
	nombre = models.CharField( max_length=70 )
	precio = models.PositiveIntegerField( default=0 )
	descripcion = models.TextField()
	boton_comprar = models.TextField()
	foto = models.ImageField(upload_to='fotos_correas')
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre

	def boton_admin(self):
		return self.boton_comprar
	boton_admin.allow_tags = True

	def foto_admin(self):
		return "<img src='%s' width='100'></img>" % self.foto.url
	foto_admin.allow_tags = True

class Pechera(models.Model):
	nombre = models.CharField( max_length=70 )
	precio = models.PositiveIntegerField( default=0 )
	descripcion = models.TextField()
	boton_comprar = models.TextField()
	foto = models.ImageField(upload_to='fotos_pecheras')
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre

	def boton_admin(self):
		return self.boton_comprar
	boton_admin.allow_tags = True

	def foto_admin(self):
		return "<img src='%s' width='100'></img>" % self.foto.url
	foto_admin.allow_tags = True

class Collar(models.Model):
	nombre = models.CharField( max_length=70 )
	precio = models.PositiveIntegerField( default=0 )
	descripcion = models.TextField()
	boton_comprar = models.TextField()
	foto = models.ImageField(upload_to='fotos_collares')
	fecha_creacion = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre

	def boton_admin(self):
		return self.boton_comprar
	boton_admin.allow_tags = True

	def foto_admin(self):
		return "<img src='%s' width='100'></img>" % self.foto.url
	foto_admin.allow_tags = True

class Chaleco(models.Model):
	nombre = models.CharField( max_length=70 )
	precio = models.PositiveIntegerField( default=0 )
	descripcion = models.TextField()
	boton_comprar = models.TextField()
	foto = models.ImageField(upload_to='fotos_chalecos')
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return self.nombre

	def boton_admin(self):
		return self.boton_comprar
	boton_admin.allow_tags = True

	def foto_admin(self):
		return "<img src='%s' width='100'></img>" % self.foto.url
	foto_admin.allow_tags = True