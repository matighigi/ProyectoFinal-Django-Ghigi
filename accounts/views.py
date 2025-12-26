from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView


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
