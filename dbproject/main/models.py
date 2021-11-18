from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class  AllFields(models.Model):
    strings = models.CharField("Chars",blank=True, max_length=20)#belgilar
    texts = models.TextField("Text") #matnlar
    email = models.EmailField("Email",blank=True, max_length=100) # email manzil
    url = models.URLField("URL",blank=True, max_length=100)
    slug = models.SlugField("*",unique=True)
    yesorno  = models.BooleanField("on/off",default=True)
    number = models.IntegerField("Integer") #butun son qabul qiladi
    # SmallIntegerField 16 bitli son , BigIntegerField 64 bitli son
    # PositiveIntegerField musbat 32 bitli son
    # PositiveSmallIntegerField musbat 16 bitli son
    floatNumber = models.FloatField("Float")#1.2 , 99.9
    decimalNumber = models.DecimalField("Decimal", max_digits=4,decimal_places=2)#99,99
    date = models.DateField("Date",auto_now_add=True)
    dateAndTime = models.DateTimeField("Date and Time",auto_now=True)

    def __str__(self):
        return f"{self.id}"

class Room(models.Model):
    number = models.IntegerField("Xona raqami", default=0)

    def __str__(self):
        return f"{self.number}"

class Teacher(models.Model):
    name = models.CharField("Ism", max_length=50)
    age = models.PositiveIntegerField("Yosh", default=0)

    def __str__(self):
        return f"{self.name}"
    # ForeignKey , ManyToManyField, OneToOneField
class Student(models.Model):
    name = models.CharField("Ism", max_length=50)
    age = models.PositiveIntegerField("Yosh", default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}"


class MyUser(models.Model):
    is_admin = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"



class Detal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class Machine(models.Model):
    name = models.CharField(max_length=50)
    detals = models.ManyToManyField(Detal)

    def __str__(self):
        return f"{self.name}"

# task 1
#     School
#     project:
#     Modellar: Teacher, Student, Room
#     Templates: index.html, teacher.html, students.html, rooms.html
#     indexda hamma malumotla  chiqadi
#     roomsda shu xonada  qaysi  studentlar va  qaysi teacher dars  otadi chiqadi
#     teachersda  hamma teacherla royhati students da hamma studentla  royhati