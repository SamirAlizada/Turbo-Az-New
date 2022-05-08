from django.forms import ModelForm
from .models import Products, Category

class ProductForm(ModelForm):
  class Meta:
    model = Products
    fields = "__all__"

class CategoryForm(ModelForm):
  class Meta:
    model = Category
    fields = "__all__"