from django.forms import ModelForm
from .models import Anuncios

class AnunciosForm(ModelForm):
    class Meta:
        model = Anuncios
        fields = ['titulo', 'descricao', 'imagen_anuncio' ]