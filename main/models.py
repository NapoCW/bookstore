from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    FICTION = 'Fiction'
    KIDS = 'Kids'
    HORROR = 'Horror'
    SPORTS = 'Sports'
    BIOGRAPHY = 'Biography'
    TALES = 'Tales'

    CATEGORY_CHOICES = [
        (FICTION, 'Fiction'),
        (KIDS, 'Kids'),
        (HORROR, 'Horror'),
        (SPORTS, 'Sports'),
        (BIOGRAPHY, 'Biography'),
        (TALES, 'Tales'),
    ]

    name = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,  
        default=FICTION  
    )
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=Category.CATEGORY_CHOICES) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True) 
    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:30]}'