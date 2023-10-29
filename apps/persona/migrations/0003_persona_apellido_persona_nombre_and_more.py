# Generated by Django 4.2.5 on 2023-10-18 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alter_persona_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='apellido',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='persona',
            name='nombre',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre_completo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
