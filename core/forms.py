# core/forms.py
from __future__ import annotations

from django import forms


def bootstrapify_form(form: forms.Form) -> None:
    """
    Aplica clases Bootstrap 5 a todos los widgets del form.
    - inputs/textarea: form-control
    - selects: form-select
    - checkbox: form-check-input
    - file: form-control
    """
    for name, field in form.fields.items():
        widget = field.widget
        attrs = widget.attrs

        # Mantener clases existentes
        existing = attrs.get("class", "")
        classes = set(existing.split()) if existing else set()

        # Tipo de widget -> clase recomendada
        if isinstance(widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple)):
            classes.add("form-check-input")
        elif isinstance(widget, (forms.Select, forms.SelectMultiple)):
            classes.add("form-select")
        else:
            classes.add("form-control")

        # Tamaño y consistencia
        attrs["class"] = " ".join(sorted(classes))