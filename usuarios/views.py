from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import DNIAuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = DNIAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Redirige al usuario a la página deseada después de iniciar sesión.
            return redirect('nombre_de_la_vista_o_url')
    else:
        form = DNIAuthenticationForm()
    return render(request, 'registration/login_template.html', {'form': form})
