from django.db import models

# Create your models here.

# Talabar malumotlarini saqlash uchun db.sqlite3 dagi TABLE
class Students(models.Model):
    first_name = models.CharField(max_length=20) # har qanday belgilar uchun maydon
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0) # int qiymatlar uchun maydon
    adress = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name}"
