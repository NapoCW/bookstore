from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category_name>/', views.category_books, name='category_books'),
    path('book/<int:book_id>/comment/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('main/custom_admin/', views.custom_admin, name='custom_admin'),
    path('main/custom_power/', views.custom_power, name='custom_power'),
]
