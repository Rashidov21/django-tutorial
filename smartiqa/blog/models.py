from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField("Tag nomi",max_length=100,)
    slug = models.SlugField("*",max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(verbose_name="Maqola nomi",max_length=200)
    slug = models.SlugField(verbose_name="*",max_length=200, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(verbose_name="Maqola rasmi", upload_to='post_Images/')
    description = models.TextField(verbose_name='Maqoala matni')
    author = models.CharField(max_length=50,default="Admin")

    def __str__(self):
        return f"{self.title}"