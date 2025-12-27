from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

urlpatterns = [
    # /pages/ (paginas)
    path("", PageListView.as_view(), name="pages_list"),

    # /pages/create/ (creación paginas)
    path("create/", PageCreateView.as_view(), name="pages_create"),

    # /pages/1/  (detalle de paginas)
    path("<int:pk>/", PageDetailView.as_view(), name="pages_detail"),

    # /pages/1/update/ (actualización paginas)
    path("<int:pk>/update/", PageUpdateView.as_view(), name="pages_update"),

    # /pages/1/delete/ (eliminación paginas)
    path("<int:pk>/delete/", PageDeleteView.as_view(), name="pages_delete"),
]
