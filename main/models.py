from django.db import models

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
        choices=CATEGORY_CHOICES,  # This ensures a dropdown list with the specified choices
        default=FICTION  # You can set a default value, for example, Fiction
    )
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=Category.CATEGORY_CHOICES)  # Use the choices from Category model
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)  # ImageField added
    def __str__(self):
        return self.title
