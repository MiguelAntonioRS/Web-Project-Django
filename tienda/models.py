from django.db import models

# Create your models here.

class CategoriaProduct(models.Model):

    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProduct"
        verbose_name_plural="categoriaProducts"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProduct, on_delete=models.CASCADE)   
    imagen = models.ImageField(upload_to="tienda")
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="producto"
        verbose_name_plural="productos"