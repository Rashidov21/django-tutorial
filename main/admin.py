from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Contact)
admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author','id']
	list_display_links = ['title']
	prepopulated_fields = {'slug':('title',)}

	search_fields = ('title','author')
	list_filter = ('author','published')
	read_only_fields = () # faqat oqish uchun maydon - ozgartrib bomedi
	