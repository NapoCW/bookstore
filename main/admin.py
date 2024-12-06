from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'rating','cover_image')  # Display relevant fields in the admin list
    search_fields = ('title', 'author')  
    list_filter = ('category',) 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)