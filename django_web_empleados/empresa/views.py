from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Noticia, Ausencia, DiasLibres, PuestoVacante, Oferta, SolicitudSoporte
from .forms import NoticiaForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('noticias')
            else:
                error = 'Invalid username or password'
                context = {'form': form, 'error': error}
                return render(request, 'login.html', context)
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('noticias')


@login_required(login_url='/login/')
def noticias(request):
    # Obtén todas las noticias de la base de datos
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'noticias.html', context)


@login_required(login_url='/login/')
def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            print(f"Noticia creada: {noticia}")
            return redirect(reverse('noticias'))
        else:
            print(f"Formulario no válido: {form.errors}")
    else:
        form = NoticiaForm()

    context = {'form': form}
    return render(request, 'crear_noticia.html', context)


@login_required(login_url='/login/')
def ausencias(request):
    # Obtén todas las noticias de la base de datos
    ausencias = Ausencia.objects.all()

    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'ausencias.html', {'ausencias': ausencias})


@login_required(login_url='/login/')
def diaslibres(request):
    # Obtén todas las noticias de la base de datos
    diaslibres = DiasLibres.objects.all()

    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'diaslibres.html', {'diaslibres': diaslibres})


@login_required(login_url='/login/')
def puestovacante(request):
    # Obtén todas las noticias de la base de datos
    puestovacante = PuestoVacante.objects.all()

    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'puestovacante.html', {'puestovacante': puestovacante})


def oferta(request):
    # Obtén todas las noticias de la base de datos
    oferta = Oferta.objects.all()

    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'oferta.html', {'oferta': oferta})


@login_required(login_url='/login/')
def solicitudsoporte(request):
    # Obtén todas las noticias de la base de datos
    solicitudsoporte = SolicitudSoporte.objects.all()

    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'solicitudsoporte.html', {'solicitudsoporte': solicitudsoporte})

# Create your views here.
