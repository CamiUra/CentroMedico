"""
URL configuration for CentroMedico_11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Logins
    path('', views.login_view, name='login'),
    path('admin_menu/', views.admin_menu, name='admin_menu'),
    path('medic_menu/', views.medic_menu, name='medic_menu'),

    # Médicos URLs
    path('medicos/', views.medic_list, name='medic_list'),
    path('medicos/new/', views.medic_new, name='medic_new'),
    path('medicos/<str:pk>/', views.medic_detail, name='medic_detail'),
    path('medicos/<str:rut>/edit/', views.medic_edit, name='medic_edit'),
    path('medicos/delete/<str:rut>/', views.medic_delete, name='medic_delete'),

    # Productos URLs
    path('productos/', views.productos_list, name='productos_list'),
    path('productos/new/', views.productos_new, name='productos_new'),
    path('productos/<int:pk>/', views.productos_detail, name='productos_detail'),
    path('productos/<int:pk>/edit/', views.productos_edit, name='productos_edit'),
    path('productos/delete/<int:pk>/', views.productos_delete, name='productos_delete'),

    # Exámenes URLs
    path('examenes/', views.examenes_list, name='examenes_list'),
    path('examenes/new/', views.examenes_new, name='examen_new'),
    path('examenes/<int:pk>/', views.examenes_detail, name='examen_detail'),
    path('examenes/<int:pk>/edit/', views.examenes_edit, name='examenes_edit'),
    path('examenes/delete/<int:pk>/', views.examenes_delete, name='examenes_delete'),

    # Especialidades URLs
    path('especialidades/', views.especialidades_list, name='especialidades_list'),
    path('especialidades/new/', views.especialidades_new, name='especialidad_new'),
    path('especialidades/<int:pk>/', views.especialidades_detail, name='especialidad_detail'),
    path('examenes/<int:pk>/edit/', views.especialidades_edit, name='especialidades_edit'),
    path('examenes/delete/<int:pk>/', views.especialidades_delete, name='especialidades_delete'),


    # Fichas Médicas URLs
    path('fichas/', views.ficha_medica_list, name='ficha_medica_list'),    
    path('fichas/new/', views.ficha_medica_new, name='ficha_medica_new'),
    path('fichas/<int:pk>/', views.ficha_medica_detail, name='ficha_medica_detail'),
    path('fichas/<int:pk>/edit/', views.ficha_medica_edit, name='ficha_medica_edit'),
    path('fichas/delete/<int:pk>/', views.ficha_medica_delete, name='ficha_medica_delete'),
    
    #Log in
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
]
