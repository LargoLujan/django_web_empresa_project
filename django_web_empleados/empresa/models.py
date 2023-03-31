# Importamos los módulos necesarios de Django
from django.db import models
from django.contrib.auth.models import User


# Modelo para representar las noticias en la plataforma
class Noticia(models.Model):
    # Campos de la noticia: título, contenido, fecha de publicación y autor
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    # Método para representación legible del objeto Noticia
    def __str__(self):
        return self.titulo


# Modelo para representar las ausencias de los empleados
class Ausencia(models.Model):
    # Campos de la ausencia: empleado, fecha de inicio, fecha de fin y motivo
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    motivo = models.TextField()

    # método para representación legible del objeto Ausencia
    def __str__(self):
        return f'{self.empleado.username} - {self.fecha_inicio} - {self.fecha_fin}'


# Modelo para representar las bajas médicas de los empleados
class BajaMedica(models.Model):
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    motivo = models.TextField()
    documento = models.TextField()

    # método para representación legible del objeto Ausencia
    def __str__(self):
        return f'{self.empleado.username} - {self.fecha_inicio} - {self.fecha_fin} - {self.motivo}'

    # Método para representación legible del objeto PuestoVacante
    def __str__(self):
        return self.titulo


# Modelo para representar las ofertas para los empleados
class Oferta(models.Model):
    # Campos de la oferta: título, descripción, fecha de inicio y fecha de fin
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    # Método para representación legible del objeto Oferta
    def __str__(self):
        return self.titulo


# Modelo para representar los puestos vacantes en la empresa
class PuestoVacante(models.Model):
    # Campos del puesto vacante: título, descripción y fecha de publicación
    titulo = models.CharField(max_length=200)
    requisitos = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    # Método para representación legible del objeto PuestoVacante
    def __str__(self):
        return self.titulo


# Modelo para representar las solicitudes de soporte de los empleados
class SolicitudSoporte(models.Model):
    # Campos de la solicitud de soporte: empleado, título, descripción, fecha de creación y estado
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')],
                              default='abierto')

    # Método para representación legible del objeto SolicitudSoporte
    def __str__(self):
        return self.titulo
