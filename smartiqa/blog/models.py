from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField("Tag nomi",max_length=100,)
    slug = models.SlugField("*",max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"