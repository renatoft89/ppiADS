from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    razao_social = forms.CharField(max_length=66)
    cnpj_cpf = forms.CharField(max_length=19)
    endereco = forms.CharField(max_length=16)
    cidade = forms.CharField(max_length=40)
    telefone = forms.CharField(max_length=17)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['razao_social', 'cnpj_cpf','endereco', 'cidade', 'username', 'telefone', 'email', 'password1', 'password2', ]