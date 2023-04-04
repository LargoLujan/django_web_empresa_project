from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.noticias, name='inicio'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/crear/', views.crear_noticia, name='crear_noticia'),
    # path('noticias/editar/<int:pk>/', views.editar_noticia, name='editar_noticia'),
    # path('noticias/eliminar/<int:pk>/', views.eliminar_noticia, name='eliminar_noticia'),
    path('ausencias/', views.ausencias, name='ausencias'),
    path('diaslibres/', views.diaslibres, name='diaslibres'),
    path('puestovacante/', views.puestovacante, name='puestovacante'),
    path('oferta/', views.oferta, name='oferta'),
    path('solicitudsoporte/', views.solicitudsoporte, name='solicitudsoporte'),
    path('profile/', views.profile, name='profile'),
]
