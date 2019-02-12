from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.


# "category_slug" parameter to optionally filter products by a given category.


def product_list_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    # Retrieve only avaliable products.
    products = Product.objects.filter(avaliable=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail_view(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, avaliable=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})
