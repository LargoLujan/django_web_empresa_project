from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Noticia, Ausencia, DiasLibres, PuestoVacante, Oferta, SolicitudSoporte


class LoginForm(AuthenticationForm):
    """
        Formulario de inicio de sesión personalizado
        """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza los campos del formulario de inicio de sesión
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nombre de usuario'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'autor']
        exclude = ['fecha_publicacion']  # Excluye el campo fecha_publicacion


class AusenciaForm(forms.ModelForm):
    class Meta:
        model = Ausencia
        fields = ['empleado', 'fecha_inicio', 'fecha_fin', 'motivo']


class DiasLibresForm(forms.ModelForm):
    class Meta:
        model = DiasLibres
        fields = ['empleado', 'fecha_inicio', 'fecha_fin', 'motivo', 'documento']


class PuestoVacanteForm(forms.ModelForm):
    class Meta:
        model = PuestoVacante
        fields = ['titulo', 'requisitos',  'fecha_publicacion']
        exclude = ['fecha_publicacion']  # Excluye el campo fecha_publicacion


class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin']


class SolicitudSoporteForm(forms.ModelForm):
    class Meta:
        model = SolicitudSoporte
        fields = ['empleado', 'descripcion', 'fecha_creacion', 'estado']
        exclude = ['fecha_creacion'] # Excluye el campo fecha_creación
