from django.urls import path
from .views import PageListView, PageDetailView

urlpatterns = [
    # /pages/ (paginas)
    path("", PageListView.as_view(), name="pages_list"),

    # /pages/1/  (detalle de paginas)
    path("<int:pk>/", PageDetailView.as_view(), name="pages_detail"),
]
