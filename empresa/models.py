from django.db import models
from multiselectfield import MultiSelectField

class Empresa(models.Model):
    razao_social = models.CharField(max_length=66, unique=True)
    cnpj_cpf = models.CharField(max_length=19)
    endereco = models.CharField(max_length=16, null=True)
    cidade = models.CharField(max_length=40, unique=True)
    telefone = models.CharField(max_length=17)
    email = models.CharField(max_length=6, unique=True)
        
    def __str__(self):
        return self.razão_social+ ' ' + self.telefone