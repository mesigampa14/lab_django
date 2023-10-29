from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.persona.forms import PersonaForm, EstudianteForm, DocenteForm
from apps.persona.models import Estudiante, Docente


def estudiante_lista(request):
    estudiantes = Estudiante.objects.all().select_related('persona')
    return render(request, 'estudiante/lista.html',
                  {'estudiantes': estudiantes})


def estudiante_crear(request):
    if request.method == 'POST':
        # En PersonaForm se guardan los datos que provienen con el prefijo "persona". Lo mismo pasa con el form estado salud
        # https://docs.djangoproject.com/en/4.1/ref/forms/api/#prefixes-for-forms

        form_persona = PersonaForm(request.POST, prefix='persona')
        form_estudiante = EstudianteForm(request.POST, prefix='estudiante')

        if form_persona.is_valid() and form_estudiante.is_valid():
            persona_instance = form_persona.save()

            estudiante_instance = form_estudiante.save(commit=False)
            # asignar persona a estado salud
            estudiante_instance.persona = persona_instance
            estudiante_instance.save()

            messages.success(request, 'Se ha agregado al estudiante correctamente.')
            return redirect(reverse('persona:estudiante_lista'))
            # return redirect(reverse('persona:persona_detalle', args={persona_instance.id}))

    else:
        form_persona = PersonaForm(prefix='persona')
        form_estudiante = EstudianteForm(prefix='estudiante')

    return render(request, 'estudiante/form.html', {
        'form_persona': form_persona,
        'form_estudiante': form_estudiante
    })


def estudiante_detalle(request, pk):
    estudiante = get_object_or_404(Estudiante.objects.select_related('persona'), pk=pk)
    return render(request,
                  'estudiante/detalle.html',
                  {'estudiante': estudiante})


def docente_lista(request):
    docentes = Docente.objects.all().select_related('persona')
    return render(request, 'docente/lista.html',
                  {'docentes': docentes})


def docente_crear(request):
    if request.method == 'POST':
        # En PersonaForm se guardan los datos que provienen con el prefijo "persona". Lo mismo pasa con el form estado salud
        # https://docs.djangoproject.com/en/4.1/ref/forms/api/#prefixes-for-forms

        form_persona = PersonaForm(request.POST, prefix='persona')
        form_docente = DocenteForm(request.POST, prefix='docente')

        if form_persona.is_valid() and form_docente.is_valid():
            persona_instance = form_persona.save()

            docente_instance = form_docente.save(commit=False)
            # asignar persona a estado salud
            docente_instance.persona = persona_instance
            docente_instance.save()

            messages.success(request, 'Se ha agregado al docente correctamente.')
            return redirect(reverse('persona:docente_lista'))
            # return redirect(reverse('persona:persona_detalle', args={persona_instance.id}))

    else:
        form_persona = PersonaForm(prefix='persona')
        form_docente = DocenteForm(prefix='docente')

    return render(request, 'docente/form.html', {
        'form_persona': form_persona,
        'form_docente': form_docente
    })


def docente_detalle(request, pk):
    docente = get_object_or_404(Docente.objects.select_related('persona'), pk=pk)
    return render(request,
                  'docente/detalle.html',
                  {'docente': docente})
