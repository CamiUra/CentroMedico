# Generated by Django 4.2 on 2024-12-05 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id_especialidad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_especialidad', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Examenes',
            fields=[
                ('id_examen', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_examen', models.CharField(blank=True, max_length=255, null=True)),
                ('precio_examen', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(blank=True, max_length=255, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('precio_producto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('rut_medico', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre_medico', models.CharField(blank=True, max_length=255, null=True)),
                ('apellido_medico', models.CharField(blank=True, max_length=255, null=True)),
                ('id_especialidad', models.ManyToManyField(related_name='medico_especialidad', to='App.especialidades')),
            ],
        ),
        migrations.CreateModel(
            name='FichaMedica',
            fields=[
                ('id_ficha', models.AutoField(primary_key=True, serialize=False)),
                ('rut_paciente', models.CharField(max_length=20)),
                ('apellido_paciente', models.CharField(blank=True, max_length=255, null=True)),
                ('anamnesis', models.TextField(blank=True, null=True)),
                ('diagnostico', models.TextField(blank=True, null=True)),
                ('fecha_atencion', models.DateField()),
                ('id_examen', models.ManyToManyField(related_name='ficha_examenes', to='App.examenes')),
                ('id_producto', models.ManyToManyField(related_name='ficha_productos', to='App.productos')),
                ('rut_medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='App.medicos')),
            ],
        ),
    ]
