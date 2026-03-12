from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre
    
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, unique=True)
    sitio_web = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'marca'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='productos')
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, related_name='productos')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.nombre
    
class Almacen(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, unique=True)
    direccion = models.CharField(max_length=80, blank=True, null=True)
    ciudad = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        db_table = 'almacen'

    def __str__(self):
        return self.nombre
    
class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='inventario')
    almacen = models.ForeignKey('Almacen', on_delete=models.CASCADE, related_name='inventario')
    cantidad = models.IntegerField()
    stock_minimo = models.IntegerField()
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'inventario'

    def __str__(self):
        return f'{self.producto.nombre} - {self.almacen.nombre} - Cantidad: {self.cantidad}'