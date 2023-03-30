from django.urls import path
from . import views

urlpatterns = [
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/crear/', views.crear_noticia, name='crear_noticia'),
    path('ausencias/', views.ausencias, name='ausencias'),
    path('bajamedica/', views.bajamedica, name='bajamedica'),
    path('puestovacante/', views.puestovacante, name='puestovacante'),
    path('oferta/', views.oferta, name='oferta'),
    path('solicitudsoporte/', views.solicitudsoporte, name='solicitudsoporte'),
]
