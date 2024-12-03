from django.contrib import admin
from .models import Book, Category

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'rating','cover_image')  # Display relevant fields in the admin list
    search_fields = ('title', 'author')  # Add search functionality
    list_filter = ('category',)  # Allow filtering by category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display category name and description

# Register the models with custom admin settings
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)