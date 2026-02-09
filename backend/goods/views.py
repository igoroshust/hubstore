from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from .utils import q_search
from goods.models import Products


def catalog(request, cat_slug=None):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get(
        "on_sale", None
    )  # имя переменной по атрибуты name в форме
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if cat_slug == "vse-tovary":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=cat_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)  # Выводим по 3 товара на каждую страницу
    current_page = paginator.page(
        int(page)
    )  # Текущая страница, отображаемая пользователю

    context = {
        "title": "Home - Каталог",
        "goods": current_page,  # queryset урезан до количества отображаемых элементов. Объект queryset расширяется методами пагинатора (page_range и т.д.)
        "slug_url": cat_slug,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, "goods/product.html", context)
