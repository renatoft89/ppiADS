from django.db import models
from django.utils.timezone import now
from multiselectfield import MultiSelectField
from django.contrib.auth.decorators import login_required

from account.models import Account

    
class Produto(models.Model):
    nome_produto = models.CharField(max_length=66, unique=True)
    descricao = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagen_produto = models.ImageField(upload_to='produtos_photos', null=True, blank=True)
    empresa = models.ForeignKey(
        Account, blank=True, on_delete=models.PROTECT
    )
    def __str__(self):
        return self.titulo