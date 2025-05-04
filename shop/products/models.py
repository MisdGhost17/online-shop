from datetime import datetime

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product')
    description = models.TextField(null=True, blank=True, default='')
    price = models.PositiveIntegerField()
    category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'Продукт: {self.name}, ID: {self.pk}'

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'Категория: {self.name}'


class ProductImage(models.Model):
    big_image = models.ImageField(upload_to='product')
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)

class ProductCharacteristics(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=20)
    product = models.ForeignKey('Product', related_name='characteristics', on_delete=models.CASCADE)
