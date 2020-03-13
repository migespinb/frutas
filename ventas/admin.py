from django.contrib import admin
from .models import *


class FrutaAdmin(admin.ModelAdmin):
	list_display=("nombre", "cantidad", "precio_compra", "precio_venta", "unidad_medida")
	search_fields=("nombre", "cantidad", "precio_compra", "precio_venta", "unidad_medida")

class VentaAdmin(admin.ModelAdmin):
	list_display=("fruta", "cantidad", "precio_total", "fecha")
	search_fields=("fruta", "cantidad", "precio_total", "fecha")
	list_filter=("fruta", "fecha")

class AbasteceAdmin(admin.ModelAdmin):
	list_display=("fruta", "cantidad", "fecha")
	search_fields=("fruta", "cantidad", "fecha")
	list_filter=("fecha",)
	date_hierarchy="fecha"

class UsuarioAdmin(admin.ModelAdmin):
	list_display=("nombre", "direccion", "telefono")
	search_fields=("nombre", "direccion", "telefono")


admin.site.register(Fruta, FrutaAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Abastece, AbasteceAdmin)
admin.site.register(Usuario, UsuarioAdmin)

