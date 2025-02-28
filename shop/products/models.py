from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product')
    short_description = models.CharField(max_length=120, blank=True)
    description = models.TextField(null=True, blank=True, default='')
    price = models.PositiveIntegerField()
    category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT)

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