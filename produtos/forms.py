from django.forms import ModelForm
from .models import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'descricao', 'preco', 'imagen_produto']



