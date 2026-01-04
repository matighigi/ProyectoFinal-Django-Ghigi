from django import forms
from django.contrib.auth.models import User
from .models import Message
from core.forms import bootstrapify_form 


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
        
        labels = {
            "recipient": "Destinatario",
            "subject": "Asunto",
            "body": "Mensaje",
        }

        help_texts = {
            "recipient": "Seleccioná el usuario al que querés enviarle el mensaje",
            "subject": "Asunto del mensaje (opcional)",
            "body": "Escribí tu mensaje acá",
        }

        widgets = {
            "body": forms.Textarea(attrs={"rows": 6}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        bootstrapify_form(self)
