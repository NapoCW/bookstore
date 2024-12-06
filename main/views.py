from django.shortcuts import render,get_object_or_404, redirect
from .models import Book, Category, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')

def category_books(request, category_name):
    category = Category.objects.get(name=category_name)
    books = Book.objects.filter(category=category)
    return render(request, 'main/category_books.html', {'category': category, 'books': books})

def add_comment(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        text = request.POST.get('comment')
        Comment.objects.create(book=book, user=request.user, text=text)
        return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

@login_required
def custom_admin(request):
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('home')

    books = Book.objects.all()
    categories = Category.objects.all()
    users = User.objects.all()

    if request.method == 'POST':
        if 'delete_book' in request.POST:
            book_id = request.POST.get('book_id')
            Book.objects.filter(id=book_id).delete()
            messages.success(request, "Book deleted successfully!")

        elif 'add_category' in request.POST:
            category_name = request.POST.get('category_name')
            if category_name:
                Category.objects.create(name=category_name)
                messages.success(request, "Category added successfully!")
            else:
                messages.error(request, "Category name cannot be empty!")

    context = {
        'books': books,
        'categories': categories,
        'users': users,
    }
    return render(request, 'main/custom_admin.html', context)