from django.shortcuts import render
from main.models import Book

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.none()
    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'search/search.html', {'books': books, 'query': query})
