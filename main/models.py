from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField('Name', max_length=50)# BARCHA BELGILARNI QABUL QILADI
	email = models.EmailField('Email', max_length=250)# FAQAT EMAIL QABUL QILADI
	subject = models.CharField('Subject', max_length=150) 
	message = models.TextField('Message') # KO'P QATORLI MATNLARNI KIRITISH MUMKIN

	def __str__(self):
		return f"Contacted > {self.name}"