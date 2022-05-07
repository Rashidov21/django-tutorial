from django.db import models

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})

class Genre(models.Model):
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name

class Actors(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="actor_images/")
    age = models.PositiveIntegerField(default=0)
    info = models.TextField()
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return self.name





class Movie(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    poster = models.ImageField(upload_to="posters/")
    description = models.TextField()
    year = models.PositiveIntegerField(default=0, blank=False)
    genre = models.ManyToManyField(Genre, related_name='movies')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='movies')
    director =models.CharField(max_length=60)
    actors = models.ManyToManyField(Actors, related_name='movies')
    rating = models.FloatField()
    
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title
