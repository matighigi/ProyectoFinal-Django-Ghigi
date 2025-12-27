from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "created_at")
    search_fields = ("title", "subtitle")
    list_filter = ("created_at",)

