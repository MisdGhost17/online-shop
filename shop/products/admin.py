from products.models import Product, ProductCategory, ProductImage, ProductCharacteristics
from django.contrib import admin

class ProductCharacteristicsInline(admin.StackedInline):
  model = ProductCharacteristics
  extra = 0


class ProductImageInline(admin.StackedInline):
  model = ProductImage
  max_num = 10
  extra = 0


class ProductAdmin(admin.ModelAdmin):
  inlines = [ProductImageInline, ProductCharacteristicsInline,]
  readonly_fields = ['created',]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)