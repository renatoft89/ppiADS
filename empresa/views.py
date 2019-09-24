from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Empresa
from .forms import EmpresaForm

@login_required
def empresas_new(request):
    form = EmpresaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'empresas_form.html', {'form': form})


def empresas_update(request):
    return redirect('home')

def empresas_delete(request):
    return redirect('home')    