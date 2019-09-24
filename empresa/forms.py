from django import forms
from django.forms import ModelForm
from localflavor.us.forms import USZipCodeField
from .models import Empresa

class EmpresaForm(ModelForm):
    postal_code = USZipCodeField()
    class Meta:
        model = Empresa
        fields = ['razao_social', 'cnpj_cpf', 'endereco', 'cidade', 'telefone', 'email']