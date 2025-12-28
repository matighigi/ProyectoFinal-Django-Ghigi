from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    Form para editar datos del Profile.
    """
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "bio", "avatar"]

        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
        }
