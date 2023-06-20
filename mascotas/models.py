from tabnanny import verbose
from django.db import models
 
# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key = True, verbose_name = "Id de Categoria")
    nombreCategoria = models.CharField(max_length = 50, blank = True, verbose_name ="Nombre de Categoria")


    def __str__(self):
        return self.nombreCategoria #devuelve un string para acceder a los objetos almacenados

class Articulo(models.Model):
    codigo = models.CharField(primary_key = True, max_length = 8, verbose_name = "ID")
    nombre = models.CharField(max_length = 50, blank = True, verbose_name = "Marca")
    precio = models.CharField(max_length = 50, blank = True, verbose_name = "Precio")
    tipo = models.CharField(max_length = 50, blank = True, verbose_name = "Tipo")
    tamaño = models.CharField(max_length = 8, blank = True, verbose_name = "Tamaño")
    imagen = models.ImageField(upload_to = "imagenes", null = True, blank = True, verbose_name = "Imagen")
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, verbose_name = "Categoria")

    def __str__(self):
        return self.nombre

