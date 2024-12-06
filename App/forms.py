from django import forms
from .models import *

class EspecialidadesForm(forms.ModelForm):
    class Meta:
        model = Especialidades
        fields = ('nombre_especialidad',)
        labels = {
            'nombre_especialidad': 'Nombre Especialidad',
        }

class ExamenesForm(forms.ModelForm):
    class Meta:
        model = Examenes
        fields = ('nombre_examen', 'precio_examen')
        labels = {
            'nombre_examen': 'Nombre Examen',
            'precio_examen': 'Precio Examen'
        }

class MedicosForm(forms.ModelForm):
    id_especialidad = forms.ModelMultipleChoiceField(
        queryset=Especialidades.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label = "Especialidad"
    )
    class Meta:
        model = Medicos
        fields = ('rut_medico','nombre_medico', 'apellido_medico', 'id_especialidad')
        labels = {
            'rut_medico': 'RUT',
            'nombre_medico': 'Nombre',
            'apellido_medico': 'Apellido',
            'id_especialidad': 'Especialidad',
        }

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('nombre_producto', 'cantidad','precio_producto')
        labels = {
            'nombre_producto': 'Producto',
            'cantidad': 'Cantidad',
            'precio_producto': 'Precio',
        }

class FichaMedicaForm(forms.ModelForm):
    id_examen = forms.ChoiceField(
        choices=Examenes.objects.all().values_list('id_examen', 'nombre_examen'))
    id_producto = forms.ChoiceField(
        choices=Productos.objects.all().values_list('id_producto', 'nombre_producto'))
    class Meta:
        model = FichaMedica
        fields = ('rut_paciente',
                  'nombre_paciente',
                  'apellido_paciente',
                  'anamnesis',
                  'diagnostico',
                  'id_examen',
                  'id_producto',
                  'fecha_atencion',
                  )
        labels = {
            'rut_paciente': 'Rut',
            'nombre_paciente': 'Nombre',
            'apellido_paciente': 'Apellido',
            'anamnesis': 'Historia Clinica',
            'diagnostico': 'Diagnostico',
            'id_examen': 'Examen',
            'id_producto': 'Medicamentos',
            'fecha_atencion': 'Fecha Atencion',
        }
        widgets = {
            'fecha_atencion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }