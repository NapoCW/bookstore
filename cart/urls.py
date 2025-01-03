from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('change_quantity/<int:book_id>/<int:new_quantity>/', views.change_quantity, name='change_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('process_checkout/', views.process_checkout, name='process_checkout'),
]
