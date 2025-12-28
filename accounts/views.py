from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        """
        Si el formulario es válido:
        - crea el usuario
        - muestra un mensaje de éxito
        - y redirige al login
        """
        response = super().form_valid(form)
        messages.success(self.request, "Cuenta creada. Ahora podés iniciar sesión.")
        return response

"""
CBV para registrar usuarios.
    - GET: muestra el formulario
    - POST: valida y guarda el usuario
"""

# Muestra el perfil del usuario logueado.
@login_required
def profile_view(request):
    return render(request, "accounts/profile.html")

# Permite editar el perfil del usuario logueado.
@login_required
def profile_edit(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "accounts/profile_edit.html", {"form": form})