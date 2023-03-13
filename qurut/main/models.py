from django.db import models

# Create your models here.

# class bu DB da jadval
# class atrrlari bu jadval ustunlari 
 
class Category(models.Model):
    name = models.CharField(verbose_name='Turkum nomi',max_length=50)
    
    
    def __str__(self) -> str:
        return str(self.name)

 
class Review(models.Model):
    name = models.CharField(verbose_name='Foydalanuvchi ismi',max_length=100)
    comment = models.TextField()
    
    
    def __str__(self) -> str:
        return str(self.name)
    

class Product(models.Model):
    name = models.CharField('Tovar nomi',max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    
    # Related 
    # birga kop ulash product category ga biriktiladi
    category = models.ForeignKey(Category, 
                                 on_delete=models.PROTECT,
                                 verbose_name="Tovar turkumi",
                                 related_name='products')
    # review = models.ForeignKey(Review,on_delete=models.CASCADE,related_name="reviews")
    views = models.PositiveIntegerField(default=0)
    description = models.TextField()
    published = models.BooleanField(default=False)
    top = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.name)
    
    
# cat_1 = "yogli"
# cat_1.products.all()

# for p in products:
#     if p.category = 'yogli':
#         print(p)