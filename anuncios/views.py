from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Anuncios
from .forms import AnunciosForm


@login_required
def anuncios_list(request):
    anuncio = Anuncios.objects.all()
    return render(request,'anuncios.html', {'anuncios': anuncio})

@login_required
def anuncios_new(request):
    form = AnunciosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('anuncios_list')
    return render(request, 'anuncios_form.html', {'form': form})




