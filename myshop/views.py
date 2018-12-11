from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm

def HomePage(request):
    return render(request, 'myIndex.html')


def Tienda(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'tienda.html',{'category': category,
                                            'categories': categories,
                                            'products': products})



