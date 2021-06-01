from django.db import models
from django.urls import reverse
# ForeignKey = birga kop ulash
# OneToOneField = birga bir ulash
# ManyToManyField = Kopga kopga ulash

class Category(models.Model):
	name = models.CharField('Category name', max_length=100)
	slug = models.SlugField('*', max_length=100, unique=True)

	def __str__(self):
		return f"{self.name}"

class Tags(models.Model):
	name = models.CharField('Tag name', max_length=100)
	slug = models.SlugField('*', max_length=100, unique=True)

	def __str__(self):
		return f"{self.name}"



class Post(models.Model):
	title = models.CharField('Title', max_length=300)
	slug = models.SlugField('*', max_length=100, unique=True)
	author = models.CharField('Author', max_length=80)
	image = models.ImageField('Poster', upload_to='posters/')
	body = models.TextField('Body')
	published = models.DateTimeField(auto_now_add=True)
	# on_delete=models.PROTECT => Ximoyalanadi  
	# on_delete=models.CASCADE => Kaskad , bir-biriga bogliq
	# on_delete=models.SET_NULL => korsatilmagan - aloqasiz
	tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.title}"

	def get_absolute_url(self):
		return reverse('main:post_detail', kwargs={'post_slug':self.slug})



# Create your models here.
class Contact(models.Model):
	name = models.CharField('Name', max_length=50)# BARCHA BELGILARNI QABUL QILADI
	email = models.EmailField('Email', max_length=250)# FAQAT EMAIL QABUL QILADI
	subject = models.CharField('Subject', max_length=150) 
	message = models.TextField('Message') # KO'P QATORLI MATNLARNI KIRITISH MUMKIN

	def __str__(self):
		return f"Contacted > {self.name}"