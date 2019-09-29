from django.db import models
from multiselectfield import MultiSelectField
from account.models import Account

class Anuncios(models.Model):
    titulo = models.CharField(max_length=66, unique=True)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    imagen_anuncio = models.ImageField(upload_to='anuncios_photos', null=True, blank=True)

    def __str__(self):
        return self.titulo