from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from apps.persona.forms import PersonaForm, EstudianteForm
from apps.persona.models import Estudiante

def mi_vista (request):
    return render(request, 'persona/index.html')

def estudiante_lista (request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante/lista.html',
                  {'estudiantes': estudiantes})

def estudiante_crear (request):

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
            return redirect(reverse('persona:persona_detalle', args={persona_instance.id}))

    else:
        form_persona = PersonaForm(prefix='persona')
        form_estudiante = EstudianteForm(prefix='estudiante')

    return render(request, 'estudiante/estudiante_form.html', {
        'form_persona': form_persona,
        'form_estudiante': form_estudiante
    })
