from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    """
    Modelo principal:
    - 2 CharField: title y subtitle
    - Texto enriquecido: content (CKEditor)
    - Imagen: image
    - Fecha: created_at
    """
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=180)
    content = RichTextField()  # texto enriquecido
    image = models.ImageField(upload_to="pages/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
