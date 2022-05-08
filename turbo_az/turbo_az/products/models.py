from django.db import models
from account.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to = 'product')
    product_price = models.PositiveIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    likes = models.ManyToManyField(User, related_name="product_like")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


    def __str__(self):
        return self.product_name