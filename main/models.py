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

	def get_absolute_url(self):
		return reverse('main:category_detail', kwargs={'category_id':self.id})


class Tags(models.Model):
	name = models.CharField('Tag name', max_length=100)
	slug = models.SlugField('*', max_length=100, unique=True)

	def __str__(self):
		return f"{self.name}"

	def get_absolute_url(self):
		return reverse('main:tag_detail', kwargs={'tag_slug':self.slug})




class Post(models.Model):
	title = models.CharField('Title', max_length=300)
	slug = models.SlugField('*', max_length=100, unique=True)
	author = models.CharField('Author', max_length=80)
	image = models.ImageField('Poster', upload_to='posters/')
	body = models.TextField('Body')
	views = models.PositiveIntegerField('Korildi', default=0)
	published = models.DateTimeField(auto_now_add=True)
	# on_delete=models.PROTECT => Ximoyalanadi  
	# on_delete=models.CASCADE => Kaskad , bir-biriga bogliq
	# on_delete=models.SET_NULL => korsatilmagan - aloqasiz
	# on_delete=models.DO_NOTHING => hech qanday amal bajarmedi
	# on_delete=models.SET_DEFAULT => doimiy korsatilgan amal boyicha ulanish

	category = models.ForeignKey(Category,
		on_delete=models.CASCADE,
		related_name='posts')
	tag = models.ManyToManyField(Tags)

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

class Comment(models.Model):
	post = models.ForeignKey(Post,
	on_delete=models.CASCADE,
	related_name='comments')
	date = models.DateTimeField('Bildirilgan sana',
		auto_now_add=True,
		null=True)
	name = models.CharField('Ismingiz', max_length=50)
	email = models.EmailField('Email')
	subject = models.CharField('Mavzu', max_length=150)
	comment = models.TextField('Xabar matni')

	def __str__(self):
		return f"{self.name}"

	class Meta:
		verbose_name = 'Muhokama'
		verbose_name_plural = 'Muhokamalar'