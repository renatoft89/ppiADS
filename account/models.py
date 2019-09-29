from django.db import models

class Account(models.Model):
    razao_social = models.CharField(max_length=66)
    cnpj_cpf = models.CharField(max_length=19)
    endereco = models.CharField(max_length=16)
    cidade = models.CharField(max_length=40)
    telefone = models.CharField(max_length=17)
    email = models.EmailField()

    def __str__(self):
        return self.razao_social