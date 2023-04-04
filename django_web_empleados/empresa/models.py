from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


# Modelo de usuario personalizado
class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_user_permissions")


# Modelo de usuario con atributos adicionales
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dni = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True)
    telefono = models.CharField(max_length=20)
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


# Modelo de noticia
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    enlace = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo


# Modelo de ausencia
class Ausencia(models.Model):
    empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    motivo = models.TextField()

    def __str__(self):
        return f'{self.empleado.username} - {self.fecha_inicio} - {self.fecha_fin}'


# Modelo de días libres
class DiasLibres(models.Model):
    empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    motivo = models.TextField()
    documento = models.TextField()

    def __str__(self):
        return f'{self.empleado.nombre} - {self.fecha_inicio} - {self.fecha_fin} - {self.motivo}'


# Modelo de oferta
class Oferta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.titulo


# Modelo de puesto vacante
class PuestoVacante(models.Model):
    titulo = models.CharField(max_length=200)
    requisitos = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


# Modelo de solicitud de soporte
class SolicitudSoporte(models.Model):
    empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')],
                              default='abierto')

    def __str__(self):
        return self.titulo
