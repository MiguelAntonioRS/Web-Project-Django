from django.contrib import admin
from .models import CategoriaProduct,Producto

# Register your models here.

class CategoriaProductAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class ProductAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(CategoriaProduct, CategoriaProductAdmin)
admin.site.register(Producto, ProductAdmin)