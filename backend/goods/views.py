from django.shortcuts import render

def catalog(request):
    """Каталог"""
    return render(request, 'goods/catalog.html')

def product(request):
    """Товар"""
    return render(request, 'goods/product.html')