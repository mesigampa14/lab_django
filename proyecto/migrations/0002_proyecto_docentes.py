# Generated by Django 4.2.5 on 2023-11-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_alter_persona_dni_docente'),
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='docentes',
            field=models.ManyToManyField(related_name='proyectos', to='persona.docente'),
        ),
    ]
