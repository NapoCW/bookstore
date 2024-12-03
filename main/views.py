from django.shortcuts import render
from .models import Book, Category

def home(request):
    return render(request, 'main/home.html')

def category_books(request, category_name):
    category = Category.objects.get(name=category_name)
    books = Book.objects.filter(category=category)
    return render(request, 'main/category_books.html', {'category': category, 'books': books})
