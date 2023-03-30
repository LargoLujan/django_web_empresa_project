from django import forms
from .models import Noticia, Ausencia, BajaMedica, PuestoVacante, Oferta, SolicitudSoporte

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'autor']
        exclude = ['fecha_publicacion']  # Excluye el campo fecha_publicacion

class AusenciaForm(forms.ModelForm):
    class Meta:
        model = Ausencia
        fields = ['empleado', 'fecha_inicio', 'fecha_fin', 'motivo']

class BajaMedicaForm(forms.ModelForm):
    class Meta:
        model = BajaMedica
        fields = ['empleado', 'fecha_inicio', 'fecha_fin', 'motivo', 'documento']

class PuestoVacanteForm(forms.ModelForm):
    class Meta:
        model = PuestoVacante
        fields = ['titulo', 'descripcion', 'requisitos', 'fecha_publicacion']

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'condiciones']

class SolicitudSoporteForm(forms.ModelForm):
    class Meta:
        model = SolicitudSoporte
        fields = ['empleado', 'asunto', 'descripcion', 'fecha_solicitud', 'estado']
