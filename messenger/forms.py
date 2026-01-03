from django import forms
from django.contrib.auth.models import User
from .models import Message


class MessageForm(forms.ModelForm):
    """
    Formulario para enviar un mensaje:
    - El usuario elige destinatario
    - Opcional: asunto
    - Mensaje: body
    """
    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Para",
        empty_label="Elegí un usuario..."
    )

    class Meta:
        model = Message
        fields = ["recipient", "subject", "body"]
        widgets = {
            "subject": forms.TextInput(attrs={"placeholder": "Asunto (opcional)"}),
            "body": forms.Textarea(attrs={"rows": 5, "placeholder": "Escribí tu mensaje..."}),
        }
