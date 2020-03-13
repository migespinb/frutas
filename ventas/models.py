from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fruta(models.Model):
	nombre=models.CharField(max_length=100, verbose_name="Nombre")
	cantidad=models.IntegerField()
	precio_compra=models.IntegerField(verbose_name="Precio compra")
	precio_venta=models.IntegerField(verbose_name="Precio venta")
	unidad_medida=models.CharField(null=True, max_length=50, verbose_name="U. Medida")

	def __str__(self):
		return self.nombre


class Venta(models.Model):
	fruta=models.ForeignKey(Fruta, null= True, on_delete=models.SET_NULL)
	cantidad=models.IntegerField()
	precio_total=models.IntegerField(verbose_name="Precio total")
	fecha=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "fruta %s , cantidad %s" %(self.fruta, self.cantidad)

class Abastece(models.Model):
	fruta=models.ForeignKey(Fruta, null= True, on_delete=models.SET_NULL)
	cantidad=models.IntegerField()
	fecha=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "fruta %s , cantidad %s" %(self.fruta, self.cantidad)

class Usuario(models.Model):
	user=models.OneToOneField(User, null=True, blank=True ,on_delete=models.CASCADE)
	nombre=models.CharField(max_length=30, verbose_name="Nombre")
	direccion=models.CharField(null=True, max_length=50, verbose_name='Direccion')
	email=models.EmailField(max_length=80, blank=True, null=True, verbose_name='Email')
	telefono=models.CharField("phone", null=True, max_length=12)
	imagen=models.ImageField( default="defecto.png",null=True, blank=True)