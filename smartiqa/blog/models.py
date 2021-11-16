from django.db import models
from django.urls import reverse

# Create your models here.
class Tag(models.Model):
    name = models.CharField("Tag nomi",max_length=100,)
    slug = models.SlugField("*",max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField("Kategoriya nomi",max_length=100,)
    slug = models.SlugField("*",max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("blog:category_detail",kwargs={"category_slug":self.slug})

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(verbose_name="Maqola nomi",max_length=200)
    slug = models.SlugField(verbose_name="*",max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(verbose_name="Maqola rasmi", upload_to='post_Images/')
    description = models.TextField(verbose_name='Maqoala matni')
    author = models.CharField(max_length=50,default="Admin")

    def get_absolute_url(self):
        return reverse("blog:post_detail",kwargs={"post_slug":self.slug})

    def __str__(self):
        return f"{self.title}"

