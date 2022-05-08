from pyexpat import model
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Products, Category
from django.http import HttpResponseRedirect
from .forms import ProductForm
from django.views.generic import ListView
from django.db.models import Q

def index(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        search = request.POST.get("search")
        results = Products.objects.filter(Q(product_name__icontains=search))

        context = {
        'results' : results
        }

        return render(request, 'products.html', context)

    context = {
        'products' : products,
        'categories' : categories

    }

    return render(request, 'products.html', context)

def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {
        'product' : product
    }

    return render(request, 'product_detail.html', context)

def category_detail(request, pk):
    # product = Products.objects.get(pk=pk)
    # context = {
    #     'product' : product
    # }

    # return render(request, 'product_detail.html', context)

    category = Category.objects.get(pk=pk)
    products = Products.objects.filter(category=category)
    categories = Category.objects.all()

    context = {
        'products' : products,
        'category' : category,
        'categories' : categories
    }
    return render(request, 'category.html', context)

def product_like(request, pk):
    product = get_object_or_404(Products, id=request.Products.get('product.pk'))
    product.likes.add(request.user)

    return HttpResponseRedirect(reverse('product-detail'), args=[str(pk)])

def create_product(request):
  form = ProductForm()
  if request.method == "POST":
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      return redirect("dash_products")
  
  context = {
    'form' : form
  }

  return render(request, 'create_product.html', context) 

def dash_products(request):
  products = Products.objects.all()

  context = {
    "products" : products,
  }

  return render(request, "dash_products.html", context)

def update_product(request, pk):
    blog = Products.objects.get(pk=pk)
    form = ProductForm(instance=blog)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, "update_product.html", context)

def delete_product(request, pk):
    blog = Products.objects.get(pk=pk)
    blog.delete()
    return redirect('index')

def dynamic_articles_view(request):
    search = Products.objects.filter(product_name__contains='Terry')
    context = {
      'search' : search
    }
    return render(request, "product_detail.html", context)
