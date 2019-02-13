from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cdata = form.cleaned_data
        cart.add(product=product,
                 quantity=cdata['quantity'],
                 update_quantity=cdata['update'])
    return redirect('cart:cart_detail_view')


def cart_remove_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail_view')


def cart_detail_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
