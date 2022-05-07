from django.db import models

# Create your models here.
class Category(models.Model):
    """Model definition for Category."""
    name = models.CharField("Category name", max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return f"{self.name}"

class Genre(models.Model):
    """Model definition for Genre."""
    name = models.CharField("Genre name", max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Genre."""

        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        """Unicode representation of Genre."""
        return f"{self.name}"

class Actor(models.Model):
    """Model definition for Actor."""
    name = models.CharField("Actor name", max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    age = models.PositiveIntegerField("Actor age",default=0)
    image = models.ImageField("Actor image", upload_to='actor_images/')
    # TODO: Define fields here

    class Meta:
        """Meta definition for Actor."""

        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'

    def __str__(self):
        """Unicode representation of Actor."""
        return f"{self.name}"

class Movie(models.Model):
    """Model definition for Movie."""
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='movie_category')
    poster = models.ImageField(upload_to='movie_posters/%Y/%m')
    title = models.CharField("Movie title", max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    description =models.TextField()
    short_description = models.CharField("Short title", max_length=550)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    quality = models.CharField("Quality", max_length=50)
    duration = models.CharField("Duration", max_length=50)
   

    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Movie."""

        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        """Unicode representation of Movie."""
        return f"{self.title}"



