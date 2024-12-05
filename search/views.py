# views.py
from django.shortcuts import render
from main.models import Book  # Import Book model

def search_books(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    books = Book.objects.none()
    if query:
        # Search for books that contain the query in their title or author
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'search/search.html', {'books': books, 'query': query})
