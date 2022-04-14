from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    prepopulated_fields = {"slug":('name',)}
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    prepopulated_fields = {"slug": ('name',)}
    
    
admin.site.register(Actors)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    prepopulated_fields = {"slug": ('title',)}