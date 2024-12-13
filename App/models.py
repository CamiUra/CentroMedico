from django.db import models

class Especialidades(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_especialidad or "Sin nombre"
    
class Examenes(models.Model):
    id_examen = models.AutoField(primary_key=True)
    nombre_examen = models.CharField(max_length=255, blank=True, null=True)
    precio_examen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nombre_examen or "Sin nombre"

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nombre_producto or "Sin nombre"
    
class Medicos(models.Model):
    rut_medico = models.CharField(primary_key=True, max_length=20)
    nombre_medico = models.CharField(max_length=255, blank=True, null=True)
    apellido_medico = models.CharField(max_length=255, blank=True, null=True)
    id_especialidad = models.ManyToManyField(Especialidades, related_name="medico_especialidad")

    def __str__(self):
        return f"{self.nombre_medico} {self.apellido_medico}"
    
class FichaMedica(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    rut_paciente = models.CharField(max_length=20)
    nombre_paciente = models.CharField(max_length=255, blank=True, null=True)
    apellido_paciente = models.CharField(max_length=255, blank=True, null=True)
    rut_medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    anamnesis = models.TextField(blank=True, null=True)
    diagnostico = models.TextField(blank=True, null=True)
    id_examen = models.ForeignKey(Examenes, on_delete=models.CASCADE, blank=True, null=True)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE, blank=True, null=True)
    fecha_atencion = models.DateField()

    def __str__(self):
        return f"Ficha: {self.id_ficha}, Paciente: {self.nombre_paciente or 'Sin nombre'}"