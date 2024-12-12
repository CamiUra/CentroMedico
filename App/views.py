from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *

#Log in
def login_view(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        clave = request.POST.get('clave')
        usuario = authenticate(request, username=rut, password=clave)
        if usuario is not None and usuario.is_superuser:
            login(request, usuario)
            return redirect('admin_menu')
        elif usuario is not None:
            login(request, usuario)
            return redirect('medic_menu')
        else:
            return render(request, 'App/login_view.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'App/login_view.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_menu(request):
    return render(request, 'App/admin_menu.html')

@login_required
def medic_menu(request):
    medic = Medicos.objects.get(rut_medico=request.user.username)
    return render(request, 'App/medic_menu.html', {})

#CRUD Medic Views
def medic_list(request):
    medicos = Medicos.objects.all()
    return render(request, 'App/medic_list.html', {'medic_list': medicos})

def medic_detail(request, pk):
    medico = get_object_or_404(Medicos, pk=pk)
    return render(request, 'App/medic_detail.html', {'medico': medico})

def medic_new(request):
    if request.method == "POST":
        form = MedicosForm(request.POST)
        if form.is_valid():
            medico = form.save()
            rut = medico.rut_medico
            password = 'KLG'+ rut[:4]
            User.objects.create_user(username=rut, password=password)
            return redirect('medic_detail', pk=medico.pk)
    else:
        form = MedicosForm()
    return render(request, 'App/medic_edit.html', {'form': form})
        
def medic_edit(request, rut):
    medico = get_object_or_404(Medicos, rut_medico=rut)
    if request.method == "POST":
        form = MedicosForm(request.POST, instance=medico)
        if form.is_valid():
            medico = form.save()
            return redirect('medic_detail', pk=medico.pk)
    else:
        form = MedicosForm(instance=medico)
    return render(request, 'App/medic_edit.html', {'form': form})
        
def medic_delete(request, rut):
    medico = get_object_or_404(Medicos, rut_medico=rut)
    if request.method == "POST":
        medico.delete()
        return redirect('medic_list')
    return render(request, 'App/medic_detail.html', {'medico': medico})

#CRUD Productos

def productos_list(request):
    productos = Productos.objects.all()
    return render(request, 'App/productos_list.html', {'productos_list': productos})

def productos_detail(request, pk):
    producto = get_object_or_404(Productos, pk=pk)
    return render(request, 'App/productos_detail.html', {'producto': producto})

def productos_new(request):
    if request.method == "POST":
        form = ProductosForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('productos_detail', pk=producto.pk)
    else:
        form = ProductosForm()
    return render(request, 'App/productos_edit.html', {'form': form})

def productos_edit(request, pk):
    producto = get_object_or_404(Productos, pk=pk)
    if request.method == "POST":
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            return redirect('productos_detail', pk=producto.pk)
    else:
        form = ProductosForm(instance=producto)
    return render(request, 'App/productos_edit.html', {'form': form})
    
def productos_delete(request, pk):
    producto = get_object_or_404(Productos, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('productos_list')
    return render(request, 'App/productos_detail.html', {'producto': producto})

#CRUD Examenes

def examenes_list(request):
    examenes = Examenes.objects.all()
    return render(request, 'App/examenes_list.html', {'examenes_list': examenes})

def examenes_detail(request, pk):
    examen = get_object_or_404(Examenes, pk=pk)
    return render(request, 'App/examenes_detail.html', {'examen': examen})

def examenes_new(request):
    if request.method == "POST":
        form = ExamenesForm(request.POST)
        if form.is_valid():
            examen = form.save()
            return redirect('examen_detail', pk=examen.pk)
    else:
        form = ExamenesForm()
    return render(request, 'App/examenes_edit.html', {'form': form})
    
def examenes_edit(request, pk):
    examen = get_object_or_404(Examenes, pk=pk)
    if request.method == "POST":
        form = ExamenesForm(request.POST, instance=examen)
        if form.is_valid():
            examen = form.save()
            return redirect('examen_detail', pk=examen.pk)
    else:
        form = ExamenesForm(instance=examen)
    return render(request, 'App/examenes_edit.html', {'form': form})
    
def examenes_delete(request, pk):
    examen = get_object_or_404(Examenes, pk=pk)
    if request.method == "POST":
        examen.delete()
        return redirect('examenes_list')
    return render(request, 'App/examenes_detail.html', {'examen': examen})

#CRUD Especialidades

def especialidades_list(request):
    especialidades = Especialidades.objects.all()
    return render(request, 'App/especialidades_list.html', {'especialidades_list': especialidades})

def especialidades_detail(request, pk):
    especialidad = get_object_or_404(Especialidades, pk=pk)
    return render(request, 'App/especialidades_detail.html', {'especialidad': especialidad})

def especialidades_new(request):
    if request.method == "POST":
        form = EspecialidadesForm(request.POST)
        if form.is_valid():
            especialidad = form.save()
            return redirect('especialidad_detail', pk=especialidad.pk)
    else:
        form = EspecialidadesForm()
    return render(request, 'App/especialidades_edit.html', {'form': form})
        
def especialidades_edit(request, pk):
    especialidad = get_object_or_404(Especialidades, pk=pk)
    if request.method == "POST":
        form = EspecialidadesForm(request.POST, instance=especialidad)
        if form.is_valid():
            especialidad = form.save()
            return redirect('especialidad_detail', pk=especialidad.pk)
    else:
        form = EspecialidadesForm(instance=especialidad)
    return render(request, 'App/especialidades_edit.html', {'form': form})
    
def especialidades_delete(request, pk):
    especialidad = get_object_or_404(Especialidades, pk=pk)
    if request.method == "POST":
        especialidad.delete()
        return redirect('especialidades_list')
    return render(request, 'App/especialidades_detail.html', {'especialidad': especialidad})

#CRUD Ficha Médica

@login_required
def ficha_medica_list(request):
    fichas_medicas = FichaMedica.objects.all()
    return render(request, 'App/ficha_medica_list.html', {'ficha_medica_list': fichas_medicas})

@login_required
def ficha_medica_detail(request, pk):
    ficha_medica = get_object_or_404(FichaMedica, pk=pk)
    examen = ficha_medica.id_examen  # Directly access the single exam instance
    producto = ficha_medica.id_producto  # Directly access the single product instance
    return render(request, 'App/ficha_medica_detail.html', {
        'ficha_medica': ficha_medica,
        'examen': examen,
        'producto': producto,
    })

@login_required
def ficha_medica_new(request):
    if request.method == "POST":
        form = FichaMedicaForm(request.POST)
        if form.is_valid():
            # Get the logged-in user's medic information
            medic = get_object_or_404(Medicos, rut_medico=request.user.username)
            ficha_medica = form.save(commit=False)
            ficha_medica.rut_medico = medic  # Set the medic for the ficha
            ficha_medica.save()  # Save the ficha_medica instance
            return redirect('ficha_medica_detail', pk=ficha_medica.pk)  # Redirect to detail view
    else:
        form = FichaMedicaForm()
    
    # Get the logged-in user's medic information
    medic = get_object_or_404(Medicos, rut_medico=request.user.username)

    return render(request, 'App/ficha_medica_edit.html', {'form': form, 'medic': medic})
    
def ficha_medica_edit(request, pk):
    ficha_medica = get_object_or_404(FichaMedica, pk=pk)
    if request.method == 'POST':
        form = FichaMedicaForm(request.POST, instance=ficha_medica)
        if form.is_valid():
            # Ensure that the foreign key fields are valid
            try:
                form.save()
                return redirect('ficha_medica_list')  # Redirect after saving
            except:
                form.add_error(None, "Error saving the form. Please check the foreign key fields.")
    else:
        form = FichaMedicaForm(instance=ficha_medica)

    return render(request, 'App/ficha_medica_edit.html', {'form': form, 'ficha_medica': ficha_medica})
    
def ficha_medica_delete(request, pk):
    ficha_medica = get_object_or_404(FichaMedica, pk=pk)
    if request.method == "POST":
        ficha_medica.delete()
        return redirect('ficha_medica_list')  # Ensure this matches the name in urls.py
    return render(request, 'App/ficha_medica_detail.html', {'ficha_medica': ficha_medica})