from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.forms import bootstrapify_form

class SignupForm(UserCreationForm):
    """
    Signup: username, email, password1, password2
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        labels = {
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }

        help_texts = {
            "username": "Elegí un nombre de usuario único",
            "password1": "La contraseña debe tener al menos 8 caracteres",
            "password2": "Ingresá la misma contraseña para confirmar",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        bootstrapify_form(self)

class ProfileForm(forms.ModelForm):
    """
    Form para editar datos del Profile.
    """
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "bio", "avatar"]

        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "avatar": "Avatar",
            "bio": "Biografía",
        }

        help_texts = {
            "avatar": "Imagen de perfil (opcional)",
            "bio": "Contanos un poco sobre vos",
        }

        widgets = {
            "bio": forms.Textarea(attrs={"rows": 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        bootstrapify_form(self)