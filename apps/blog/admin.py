from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import Articulo, Imagen, ProveedorPublicidad, FormatoPublicidad, ContenidoFragmento, SideAd



class SideAdInline(admin.StackedInline):
    model = SideAd
    extra = 1
    fields = ('position', 'proveedor_publicidad', 'orden')
    autocomplete_fields = ['proveedor_publicidad']

class ContenidoFragmentoForm(forms.ModelForm):
    class Meta:
        model = ContenidoFragmento
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        proveedor = cleaned_data.get('proveedor_publicidad')
        imagen = cleaned_data.get('imagen')
        texto = cleaned_data.get('texto')
        
        # Validar que al menos un campo de contenido esté presente
        if not any([texto, imagen, proveedor]):
            raise forms.ValidationError("Debe proporcionar texto, imagen o proveedor de publicidad")
        
        return cleaned_data

class ContenidoFragmentoInline(admin.StackedInline):
    model = ContenidoFragmento
    form = ContenidoFragmentoForm
    extra = 1
    fields = ('orden', 'texto', 'imagen', 'proveedor_publicidad')
    autocomplete_fields = ['imagen', 'proveedor_publicidad']
    
    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.validate_min = True
        return formset

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    inlines = [ContenidoFragmentoInline, SideAdInline]  # <-- Agrega aquí el nuevo inline
    list_display = ('title', 'descripcion', 'image_preview', 'creacion')
    search_fields = ('title', 'descripcion')
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;">', obj.image.url)
        return "-"
    image_preview.short_description = "Vista previa"

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('imagen_preview', 'descripcion', 'creado')
    search_fields = ('descripcion',)
    readonly_fields = ('imagen_preview',)
    
    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="max-height: 100px;">', obj.imagen.url)
        return "-"
    imagen_preview.short_description = "Vista previa"

class FormatoPublicidadInline(admin.TabularInline):
    model = FormatoPublicidad
    extra = 1
    fields = ('tipo', 'codigo')

@admin.register(ProveedorPublicidad)
class ProveedorPublicidadAdmin(admin.ModelAdmin):
    inlines = [FormatoPublicidadInline]
    list_display = ('nombre', 'formatos_publicidad')
    search_fields = ('nombre',)
    
    def formatos_publicidad(self, obj):
        return ", ".join([f.get_tipo_display() for f in obj.formatopublicidad_set.all()])
    formatos_publicidad.short_description = "Formatos disponibles"


