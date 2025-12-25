from django.shortcuts import render, redirect
from blog.models import Post
from .forms import AutorForm, CategoriaForm, PostForm

# Vista para la página de inicio del blog
def inicio(request):
    return render(request, "blog/inicio.html")


# Vista para crear un Autor nuevo
def crear_autor(request):

    # Si el usuario envió el formulario, creamos el autor con los datos
    if request.method == "POST":
        formulario = AutorForm(request.POST)

        #Verificamos que los datos sean válidos
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
        
    # Si no, mostramos el formulario vacío    
    else:
        formulario = AutorForm()

    return render(request, "blog/crear_autor.html", {"form": formulario})

# Vista para crear una Categoría nueva
def crear_categoria(request):
    if request.method == "POST":
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = CategoriaForm()

    return render(request, "blog/crear_categoria.html", {"form": formulario})


# Vista para crear un Post nuevo
def crear_post(request):
    if request.method == "POST":
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = PostForm()

    return render(request, "blog/crear_post.html", {"form": formulario})

# Vista para buscar Posts por título
def buscar_post(request):
    # Tomamos lo que el usuario escribió en el campo "q" del formulario (query)
    termino = request.GET.get("q", "")

    resultados = []
    if termino:
        # Buscamos en la BD posts cuyo título contenga el término
        resultados = Post.objects.filter(titulo__icontains=termino)

    # Enviamos al template tanto el término como la lista de resultados
    return render(request, "blog/buscar_post.html", {
        "termino": termino,
        "resultados": resultados,
    })