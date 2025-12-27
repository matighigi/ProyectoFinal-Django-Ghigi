from django.views.generic import ListView, DetailView
from .models import Page

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
