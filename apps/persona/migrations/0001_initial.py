# Generated by Django 4.2.5 on 2023-10-16 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('nombre_completo', models.CharField(max_length=200)),
                ('mail', models.EmailField(blank=True, max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], max_length=9)),
                ('domicilio', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('nombre_completo',),
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=8, unique=True)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='persona.persona')),
            ],
        ),
    ]