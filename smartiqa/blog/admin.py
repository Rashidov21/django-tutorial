from django.contrib import admin
from .models import Tag, Post
# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    prepopulated_fields = {"slug":("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','published']
    list_filter = ['id','published','author']
    prepopulated_fields = {"slug":("title",)}