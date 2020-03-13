from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class FrutaForm(forms.ModelForm):
	nombre=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-2 "}))
	cantidad=forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control py-2 "}))
	precio_compra=forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control py-2 "}))
	precio_venta=forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control py-2 "}))
	unidad_medida=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-2 "}))

	class Meta:
		model = Fruta
		fields = "__all__"


class VentaForm(forms.ModelForm):
	fruta=forms.ModelChoiceField(queryset=Fruta.objects.all().order_by('nombre'), widget = forms.Select(attrs = {'class':"form-control py-2", 'onchange':"cambiar()"}))
	cantidad=forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control py-2", 'id':"cant", 'onkeyup':"calcular_total()", 'onchange':"calcular_total()"}))
	precio_total=forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control py-2", 'id':"total", 'readonly':"readonly"}))

	class Meta:
		model = Venta
		fields = "__all__"


class AbasteceForm(forms.ModelForm):
	fruta=forms.ModelChoiceField(queryset=Fruta.objects.all().order_by('nombre'), widget = forms.Select(attrs = {'class':"form-control py-2"}))
	cantidad=forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control py-2 "}))

	class Meta:
		model = Abastece
		fields = "__all__"


class UsuarioForm(forms.ModelForm):
	nombre=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-2 "}))
	direccion=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-2 "}))
	email=forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control py-2 "}))
	telefono=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-2 "}))

	class Meta:
		model=Usuario
		fields="__all__"
		exclude=['user']


class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=["username", "email", "password1", "password2"]