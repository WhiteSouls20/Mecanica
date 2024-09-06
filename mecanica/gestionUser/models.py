from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(db_column='clienteRut', primary_key=True, max_length=10)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20, blank=True, null=True)  # Segundo nombre puede ser opcional
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)  # Apellido materno puede ser opcional
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.CharField(max_length=45)  # Cambiado a BooleanField

    def __str__(self):
        return f"{self.primer_nombre} {self.apellido_paterno}"


class Vehiculo(models.Model):  # Agregado models.Model
    rut = models.ForeignKey('Cliente', on_delete=models.CASCADE, db_column='clienteRut')
    modelo_vehiculo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    tipo_vehiculo = models.CharField(max_length=20)
    motorizacion = models.CharField(max_length=20)
    id_patente = models.AutoField(db_column='idPatente', primary_key=True)
    patente = models.CharField(max_length=20, blank=False, null=False)
    estado = models.CharField(max_length=45, blank=False, default='DEFAULT VALUE')

    def __str__(self):
        return f"{self.modelo_vehiculo} - {self.patente}"  # Combinado en un solo __str__


class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

    
# class Patente (models.Model):
    # id_patente = models.AutoField(db_column='idPatente', primary_key=True)
    # patente = models.CharField (max_length=20, blank=False, null=False)
    # def __str__ (self):
        # return str (self.patente)        