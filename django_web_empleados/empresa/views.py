from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Noticia, Ausencia, DiasLibres, PuestoVacante, Oferta, SolicitudSoporte
from .forms import NoticiaForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
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


def noticias(request):
    # Obtén todas las noticias de la base de datos
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'noticias', context)


def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.autor = request.user
            form.save()
            return HttpResponseRedirect('noticias.html')
    else:
        form = NoticiaForm()

    context = {'form': form}
    return render(request, 'crear_noticia.html', context)


def ausencias(request):
    # Obtén todas las noticias de la base de datos
    ausencias = Ausencia.objects.all()

    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'ausencias.html', {'ausencias': ausencias})


def diaslibres(request):
    # Obtén todas las noticias de la base de datos
    diaslibres = DiasLibres.objects.all()

    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'diaslibres.html', {'diaslibres': diaslibres})


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


def solicitudsoporte(request):
    # Obtén todas las noticias de la base de datos
    solicitudsoporte = SolicitudSoporte.objects.all()

    # Renderiza la plantilla noticias.html y pasa las noticias como contexto
    return render(request, 'solicitudsoporte.html', {'solicitudsoporte': solicitudsoporte})

# Create your views here.
