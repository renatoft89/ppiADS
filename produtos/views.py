from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm


def produtos_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produto': produtos})

def produtos_new(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('produtos_list')
    return render(request, 'produtos_form.html', {'form': form})