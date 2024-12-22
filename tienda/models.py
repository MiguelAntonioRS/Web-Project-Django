from django.db import models

# Create your models here.

class CategoriaProduct(models.Model):

    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProduct"
        verbose_name_="categoriaProducts"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProduct, on_delete=models.CASCADE)   
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_="Productos"