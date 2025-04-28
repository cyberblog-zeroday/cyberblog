from django.urls import path
from . import views
from .views import ArticuloView, ArticuloDetailView, ArticuloListAPIView

app_name = 'blog'

urlpatterns = [
    path("blog", ArticuloView.as_view(), name="lista-articulos"),
    path("detail/<slug:slug>/", ArticuloDetailView.as_view(), name="detalle-articulo"),
    path('test-404/', views.trigger_404),
    path('api/articulos/', ArticuloListAPIView.as_view(), name='articulo-list'),

]