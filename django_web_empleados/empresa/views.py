from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Noticia, Ausencia, DiasLibres, PuestoVacante, Oferta, SolicitudSoporte
from .forms import NoticiaForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Vista de perfil de usuario
@login_required(login_url='/login/')
def profile(request):
    context = {'user': request.user}
    return render(request, 'profile.html', context)


# Vista de inicio de sesión de usuario
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
                context = {'form': form, 'error': 'Invalid username or password'}
                return render(request, 'login.html', context)
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)


# Vista de cierre de sesión de usuario
def user_logout(request):
    logout(request)
    return redirect('login')


# Vista de lista de noticias
@login_required(login_url='/login/')
def noticias(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    return render(request, 'noticias.html', context)


# Vista de creación de noticias
@login_required(login_url='/login/')
def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.save()
            return redirect(reverse('noticias'))
    else:
        form = NoticiaForm()

    context = {'form': form}
    return render(request, 'crear_noticia.html', context)


# Vista de lista de ausencias
@login_required(login_url='/login/')
def ausencias(request):
    ausencias = Ausencia.objects.all()
    return render(request, 'ausencias.html', {'ausencias': ausencias})


# Vista de lista de días libres
@login_required(login_url='/login/')
def diaslibres(request):
    diaslibres = DiasLibres.objects.all()
    return render(request, 'diaslibres.html', {'diaslibres': diaslibres})


# Vista de lista de puestos vacantes
@login_required(login_url='/login/')
def puestovacante(request):
    puestovacante = PuestoVacante.objects.all()
    return render(request, 'puestovacante.html', {'puestovacante': puestovacante})


# Vista de lista de ofertas
def oferta(request):
    oferta = Oferta.objects.all()
    return render(request, 'oferta.html', {'oferta': oferta})


# Vista de lista de solicitudes de soporte
@login_required(login_url='/login/')
def solicitudsoporte(request):
    solicitudsoporte = SolicitudSoporte.objects.all()
    return render(request, 'solicitudsoporte.html', {'solicitudsoporte': solicitudsoporte})
