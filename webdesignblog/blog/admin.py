from django.contrib import admin
from .models import (Category,Post)
# Register your models here.
# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","id"]
    list_display_links = ["name"]
    prepopulated_fields = {
        "slug":("name",)
    }
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","author", "category"]
    list_display_links = ["title"]
    prepopulated_fields = {
        "slug":("title",)
    }