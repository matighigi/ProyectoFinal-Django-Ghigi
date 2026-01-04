from django import forms
from core.forms import bootstrapify_form
from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ("title", "subtitle", "content", "image")
        
        labels = {
            "title": "Título",
            "subtitle": "Subtítulo",
            "content": "Contenido",
            "image": "Imagen",
        }

        help_texts = {
            "title": "Título principal de la página",
            "subtitle": "Breve descripción o bajada del título",
            "content": "Contenido completo de la página",
            "image": "Imagen principal (opcional)",
        }

        widgets = {
            "content": forms.Textarea(attrs={"rows": 6}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        bootstrapify_form(self)
