from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login #cambio nombre por problema con vista login, no puede llamarse igual que el metodo
from django.contrib.auth.decorators import login_required
from django.contrib import messages	
from .decorators import unauthenticated_user, admin_only
from .models import *
from .forms import *

# Create your views here.

# Acceso
def register(request):
	if request.user.is_authenticated:
		return redirect("/")
	else:
		form=CreateUserForm()
		if request.method == "POST":
			form=CreateUserForm(request.POST)
			if form.is_valid():
				user=form.save()
				username=form.cleaned_data.get("username")
				email=form.cleaned_data.get("email")

				group=Group.objects.get(name="vendedor")
				user.groups.add(group)
				Usuario.objects.create(
					user=user,
					nombre=username,
					email=email
					)

				messages.success(request, "Registro exitoso para "+ username)
				return redirect ("/login")
		return render(request, "register.html", {"form":form})


@unauthenticated_user
def login(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")

		user=authenticate(request, username=username, password=password)

		if user is not None:
			auth_login(request, user)
			return redirect("/")
		else:
			messages.info(request, "Datos erroneos")
	return render(request, "login.html")


@login_required(login_url='/login')
def config(request):
	usuario=request.user.usuario
	form=UsuarioForm(instance=usuario)

	if request.method=="POST":
		form=UsuarioForm(request.POST, request.FILES, instance=usuario)
		if form.is_valid():
			form.save()
	return render(request, "configurar.html", {"form":form})


@login_required(login_url='/login')
def logouts(request):
	logout(request)
	return redirect("/login")


# Sistema
@login_required(login_url='/login')
@admin_only
def index(request):
	if "fecha_inicio" in request.GET and "fecha_termino" in request.GET:

		f_inicio=request.GET["fecha_inicio"]
		f_fin=request.GET["fecha_termino"]

		ventas=Venta.objects.filter(fecha__range=(f_inicio, f_fin))
		costos=venta=ingresos=0

		for v in ventas:
		    costos += v.fruta.precio_compra * v.cantidad
		    venta += v.precio_total

		ingresos=venta - costos
		return render(request, "dashboard.html", {"ventas":ventas, "costos":costos, "venta":venta, "ingresos":ingresos})
	else:
		ventas=Venta.objects.all()
		costos=venta=ingresos=0
		for v in ventas:
		    costos += v.fruta.precio_compra * v.cantidad
		    venta += v.precio_total
		ingresos=venta - costos
		return render(request, "dashboard.html", {"ventas":ventas, "costos":costos, "venta":venta, "ingresos":ingresos})


@login_required(login_url='/login')
def frutas(request):
	frutas=Fruta.objects.all()
	return render(request, "frutas.html", {"models": frutas})


@login_required(login_url='/login')
def ventas(request):
	ventas=Venta.objects.all().order_by('-fecha')
	return render(request, "ventas.html", {"models": ventas})


@login_required(login_url='/login')
@admin_only
def stocks(request):
	stocks=Abastece.objects.all().order_by('-fecha')
	return render(request, "stock.html", {"models": stocks})


# CRUDS
# frutas
@login_required(login_url='/login')
@admin_only
def createfruta(request):
	if request.method == "POST":
		model=FrutaForm(request.POST)
		if model.is_valid():
			try:
				model.save()
				return redirect ("/frutas")
			except Exception as e:
				pass
	else:
		model=FrutaForm()
		return render(request, "form_fruta.html", {"formulario":model})



@login_required(login_url='/login')
@admin_only
def viewfruta(request, id):
	model=Fruta.objects.get(id=id)
	return render(request, "temp_fruta.html", {"model":model})



@login_required(login_url='/login')
@admin_only
def updatefruta(request, id):
	modelo=Fruta.objects.get(id=id)
	model=FrutaForm(instance=modelo)

	if request.method == "POST":
		model=FrutaForm(request.POST, instance=modelo)
		if model.is_valid():
			try:
				model.save()
				return redirect ("/frutas")
			except Exception as e:
				pass
	else:
		return render(request, "form_fruta.html", {"formulario":model})



@login_required(login_url='/login')
@admin_only
def deletefruta(request, id):
	if Venta.objects.filter(fruta=id).exists():
		messages.info(request, "No se puede eliminar esta fruta porque tiene ventas asociadas")
	else:
		model=Fruta.objects.get(id=id)
		model.delete()
	return redirect ("/frutas")



# Venta
@login_required(login_url='/login')
def createventa(request):
	if request.method == "POST":
		model=VentaForm(request.POST)
		if model.is_valid():
			try:
				model.save()
				# La venta disminuye el stock
				id_fruta=request.POST.get('fruta')
				cantidad=request.POST.get('cantidad')
				fruta=Fruta.objects.get(id=id_fruta)
				fruta.cantidad=fruta.cantidad - int(cantidad)
				fruta.save()
				return redirect ("/ventas")
			except Exception as e:
				pass
	else:
		model=VentaForm()
		return render(request, "form_venta.html", {"formulario":model})



@login_required(login_url='/login')
def viewventa(request, id):
	model=Venta.objects.get(id=id)
	return render(request, "temp_venta.html", {"model":model})



@login_required(login_url='/login')
def updateventa(request, id):
	modelo=Venta.objects.get(id=id)
	cant_antes=modelo.cantidad
	stock_antes=modelo.fruta.cantidad
	if request.method == "POST":
		model=VentaForm(request.POST, instance=modelo)
		if model.is_valid():
			try:
				cant_actual=model.cleaned_data['cantidad']
				mov_stock=cant_antes - cant_actual
				id_fruta=request.POST.get('fruta')
				fruta=Fruta.objects.get(id=id_fruta)
				fruta.cantidad=fruta.cantidad + int(mov_stock)
				fruta.save()
				model.save()
				return redirect ("/ventas")
			except Exception as e:
				pass
	else:
		model=VentaForm(instance=modelo)
		return render(request, "form_venta.html", {"formulario":model})


@login_required(login_url='/login')
def deleteventa(request, id):
	model=Venta.objects.get(id=id)
	id_fruta=model.fruta.id
	cantidad=model.cantidad
	if model.delete():
		fruta=Fruta.objects.get(id=id_fruta)
		fruta.cantidad=fruta.cantidad + int(cantidad)
		fruta.save()
	return redirect ("/ventas")


# Stock
@login_required(login_url='/login')
@admin_only
def createstock(request):
	if request.method == "POST":
		model=AbasteceForm(request.POST)
		if model.is_valid():
			try:
				if model.save():
					id_fruta=request.POST.get('fruta')
					cantidad=request.POST.get('cantidad')
					fruta=Fruta.objects.get(id=id_fruta)
					fruta.cantidad=fruta.cantidad + int(cantidad)
					fruta.save()
					return redirect ("/stocks")
			except Exception as e:
				pass
	else:
		model=AbasteceForm()
		return render(request, "form_stock.html", {"formulario":model})



@login_required(login_url='/login')
@admin_only
def deletestock(request, id):
	model=Abastece.objects.get(id=id)
	id_fruta=model.fruta.id
	cantidad=model.cantidad
	# si se borra hay que quitar elementos de stock
	if model.delete():
		fruta=Fruta.objects.get(id=id_fruta)
		fruta.cantidad=fruta.cantidad - int(cantidad)
		fruta.save()
	return redirect ("/stocks")


# Ajax
def obtener_precio(request):
    id = request.GET.get('id', None)
    fruta=Fruta.objects.get(id=id)
    valor=fruta.precio_venta
    data = {
        'valor_vta': valor
    }
    return JsonResponse(data)