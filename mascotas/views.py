from django.shortcuts import render, redirect
from .models import Mascota
from .forms import MascotaForm


def home(request):
    return render(request, 'home.html')


def feed(request):
    mascotas = Mascota.objects.all().order_by('-id')[:50]
    return render(request, 'widgets/feed.html', {
        'mascotas': mascotas
    })


def reporta_mascota(request):
    form = MascotaForm(request.user)
    if request.method == "POST":
        form = MascotaForm(request.user, request.POST)
        if form.is_valid() and request.user.is_authenticated():
            form.save()
            return redirect('home')
        else:
            # return redirect with errors
            return redirect('home')
    return render(request, 'mascotas/reporta-mascota.html', {
        'form': form
    })
