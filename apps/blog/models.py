from django.db import models
from django.utils.text import slugify


class Articulo(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=255)
    image = models.FileField(upload_to="img", storage=None, max_length=100,null=True, blank=True )
    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)  # Genera el slug automáticamente
        super().save(*args, **kwargs)

class Imagen(models.Model):
    imagen = models.ImageField(
        upload_to='articulos/%Y/%m/%d/'
        )
    descripcion = models.CharField(max_length=255, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return f"{self.imagen} - {self.descripcion}"


class ProveedorPublicidad(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    codigo_base = models.TextField(blank=True)

    def get_banner_ad(self):
        return self.formatopublicidad_set.filter(tipo='BANNER').first()

    def __str__(self):
        return self.nombre

class FormatoPublicidad(models.Model):
    TIPOS_FORMATO = [
        ('POPUNDER', 'Popunder'),
        ('BANNER', 'Banner'),
        ('NATIVO', 'Nativo'),
        ('SOCIAL', 'Barra Social'),
        ('VIDEO', 'Video'),
    ]
    proveedor_publicidad = models.ForeignKey(ProveedorPublicidad, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS_FORMATO)
    codigo = models.TextField()

    def __str__(self):
        return self.proveedor_publicidad.nombre


class ContenidoFragmento(models.Model):
    
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='fragmentos')
    orden = models.PositiveIntegerField(default=0)
    texto = models.TextField(blank=True, null=True)
    proveedor_publicidad = models.ForeignKey(ProveedorPublicidad, on_delete=models.CASCADE, null=True, blank=True)

    imagen = models.ForeignKey(
        Imagen,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['orden']


    def __str__(self):
        return f"Fragmento {self.orden} - {self.articulo}"



class SideAd(models.Model):
    POSITION_CHOICES = [
        ('left', 'Izquierda'),
        ('right', 'Derecha'),
    ]
    
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='side_ads')
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    proveedor_publicidad = models.ForeignKey(ProveedorPublicidad, on_delete=models.CASCADE)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name = "Publicidad Lateral"
        verbose_name_plural = "Publicidades Laterales"

    def __str__(self):
        return f"{self.get_position_display()} - {self.proveedor_publicidad}"
