from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return f"{self.name}"
    
class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.CharField(max_length=50)
    poster = models.ImageField(upload_to="posters/")
    body = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Posts"
        
        # this models is   
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_comments')
    name = models.CharField(max_length=50)
    message = models.TextField()
    
    def __str__(self):
        return f"Comment for post/{self.post.id}"
    
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Comments"