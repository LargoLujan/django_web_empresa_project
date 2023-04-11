from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/crear/', views.crear_noticia, name='crear_noticia'),
    path('ausencias/', views.ausencias, name='ausencias'),
    path('diaslibres/', views.diaslibres, name='diaslibres'),
    path('puestovacante/', views.puestovacante, name='puestovacante'),
    path('oferta/', views.oferta, name='oferta'),
    path('solicitudsoporte/', views.solicitudsoporte, name='solicitudsoporte'),
    path('profile/', views.profile, name='profile'),
    path('registrarse/', views.registrarse, name='registrarse'),


]

