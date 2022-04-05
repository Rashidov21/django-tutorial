from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.title}"


    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Post title",
        blank=False,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    poster = models.ImageField(upload_to="post_posters/")
    author = models.CharField(
        verbose_name="Post Author",
        max_length=50,
        blank=False,
        default="Admin")
    published = models.DateTimeField(auto_now_add=True)
    description = models.TextField(verbose_name="Post Content")
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-id"]
