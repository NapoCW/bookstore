from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from main.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user) 
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user).first() 
    
    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            item.total_price = item.book.price * item.quantity 
        
        total_cart_price = sum(item.total_price for item in cart_items)
        cart_categories = set(item.book.category for item in cart_items)
        recommendations = Book.objects.filter(category__in=cart_categories).exclude(id__in=[item.book.id for item in cart_items])

        return render(request, 'cart/cart.html', {'cart_items': cart_items,'total_price': total_cart_price,'recommendations': recommendations})
    else:
        return render(request, 'cart/cart.html', {'cart_items': [],'total_price': 0,'recommendations': []})

    cart_items = CartItem.objects.filter(cart=cart)

    for item in cart_items:
        item.total_price = item.book.price * item.quantity

    total_cart_price = sum(item.total_price for item in cart_items)

    cart_book_categories = [item.book.category for item in cart_items]
    
    recommendations = Book.objects.filter(category__in=cart_book_categories).exclude(id__in=[item.book.id for item in cart_items]).distinct()

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total_cart_price': total_cart_price,
        'recommendations': recommendations,  
    })

@login_required
def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()

@login_required
def order_complete(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    cart.save()
    cart_items.delete()

    return render(request, 'cart/order_complete.html') 
@login_required
def change_quantity(request, book_id, new_quantity):
    cart = Cart.objects.get(user=request.user) 
    cart_item = get_object_or_404(CartItem, cart=cart, book__id=book_id)  
    if new_quantity <= 0:
        cart_item.delete()
        cart_item.quantity = new_quantity 
        cart_item.save()  
    return redirect(request.META.get('HTTP_REFERER', '/'))  

def checkout(request):
    return render(request, 'cart/checkout.html')

def process_checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        address = request.POST.get('address')
        billing_option = request.POST.get('billing_option')
        street_address = request.POST.get('street_address')

        return redirect('order_complete')
    else:
        return HttpResponse("Invalid request", status=400)