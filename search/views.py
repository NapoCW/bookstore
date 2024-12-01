from django.shortcuts import render
from .models import Book

def search_books(request):
    query = request.GET.get('query', '')
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query) | Book.objects.filter(category__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'search/search.html', {'books': books, 'query': query})
