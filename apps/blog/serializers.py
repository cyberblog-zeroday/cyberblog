from rest_framework.serializers import ModelSerializer
from .models import Articulo

class ArticuloSerializer(ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('__all__')