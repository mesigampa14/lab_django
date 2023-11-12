from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.movimiento.forms import MovimientoForm
from apps.proyecto.forms import ProyectoForm
from apps.proyecto.models import Proyecto


def proyecto_lista(request):
    proyectos = Proyecto.objects.all().select_related()
    return render(request, 'proyecto/lista.html',
                  {'proyectos': proyectos})


def proyecto_crear(request):
    if request.method == 'POST':
        # En PersonaForm se guardan los datos que provienen con el prefijo "persona". Lo mismo pasa con el form estado salud
        # https://docs.djangoproject.com/en/4.1/ref/forms/api/#prefixes-for-forms

        form_proyecto = ProyectoForm(request.POST, prefix='proyecto')
        form_movimiento = MovimientoForm(request.POST, prefix='estado')

        if form_proyecto.is_valid() and form_movimiento.is_valid():
            proyecto_instance = form_proyecto.save()

            estado_instance = form_movimiento.save(commit=False)
            estado_instance.proyecto = proyecto_instance
            estado_instance.tipo_movimiento = 'presenta_PTF'
            estado_instance.save()

            messages.success(request, 'Se ha agregado al proyecto correctamente.')
            return redirect(reverse('proyecto:proyecto_lista'))
            # return redirect(reverse('persona:persona_detalle', args={persona_instance.id}))

    else:
        form_proyecto = ProyectoForm(prefix='proyecto')
        form_movimiento = MovimientoForm(request.POST, prefix='estado')

    return render(request, 'proyecto/form.html', {
        'form_proyecto': form_proyecto,
        'form_estado': form_movimiento,
    })