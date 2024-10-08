from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering=('name',)
        verbose_name=('Category',)
        verbose_name_plural=('Categories',)

    def __str__(self):
        return self.name

class Product(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    name= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, unique=True)
    image= models.ImageField(upload_to='products/')
    description= models.TextField()
    price = models.IntegerField()
    available= models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name','category')
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.name