from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Genre)
class GenresAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "likes", "rating"]
    list_display_links = ["title"]
    prepopulated_fields = {"slug":("title",)}