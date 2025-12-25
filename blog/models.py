from django.db import models

# Create your models here.

# Modelo Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=50)       # Nombre del autor
    apellido = models.CharField(max_length=50)     # Apellido del autor
    email = models.EmailField(unique=True)         # Email único
    bio = models.TextField(blank=True, null=True)  # Biografía opcional

    def __str__(self):
        # Muestra cómo se ve el autor en pantalla
        return f"{self.nombre} {self.apellido}"


# Modelo Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


# Modelo Post
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    # Un autor puede tener muchos posts, pero un post tiene 1 autor
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    # Una categoria puede tener muchos posts, pero un post tiene 1 categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
