from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Page
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

#Lista de páginas: /pages/
class PageListView(ListView):
    model = Page
    template_name = "pages/page_list.html"
    context_object_name = "pages"
    ordering = ["-created_at"]

#Detalle de cada página: /pages/<id>/
class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page_detail.html"
    context_object_name = "page"

# Crear una nueva página: /pages/new/
class PageCreateView(LoginRequiredMixin, CreateView):
    """
    - LoginRequiredMixin: obliga a estar logueado
    - CreateView: Django se encarga del formulario y guardado
    """
    model = Page
    template_name = "pages/page_form.html"
    fields = ["title", "subtitle", "content", "image"]
    success_url = reverse_lazy("pages_list")
    login_url = reverse_lazy("login")

# Editar una página existente: /pages/<id>/edit/
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = "pages/page_form.html"
    fields = ["title", "subtitle", "content", "image"]
    success_url = reverse_lazy("pages_list")
    login_url = reverse_lazy("login")

# Eliminar una página: /pages/<id>/delete/
class PageDeleteView(LoginRequiredMixin, DeleteView):
    """
    Muestra una pantalla de confirmación.
    """
    model = Page
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("pages_list")
    login_url = reverse_lazy("login")
