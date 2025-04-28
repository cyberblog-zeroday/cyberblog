from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics
from .models import Articulo
from .serializers import ArticuloSerializer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404

from django.shortcuts import get_object_or_404

from .models import Articulo


# Create your views here.
class ArticuloView(ListView):
    model = Articulo
    paginate_by = 15  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista-articulos"] = timezone.now()
        return context
    
class ArticuloDetailView(DetailView):
    model = Articulo
    slug_field = 'slug'  # Campo del modelo que contiene el slug
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["detail"] = timezone.now()
        return context




def trigger_404(request):
    raise Http404("Esta es una prueba de error 404")


#  - - - - api - - - - 



class ArticuloListAPIView(generics.ListAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer