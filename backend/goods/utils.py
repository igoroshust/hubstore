from .models import Products
from django.db.models import Q


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2]  # список ключевых слов (поиск по нескольким словам)
    
    q_objects = Q()
    
    for token in keywords:
        q_objects |= Q(name__icontains=token)  # поиск по наименованию
        q_objects |= Q(description__icontains=token)  # поиск по описанию
        
    return Products.objects.filter(q_objects)