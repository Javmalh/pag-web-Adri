from django.db import models

# Create your models here.
#tablas de bd (create table contacto)

class Contacto(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)   
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nombre + ' - ' + self.user.username
    
    
    