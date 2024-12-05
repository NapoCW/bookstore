from django.shortcuts import render, redirect
from .models import Cart, CartItem
from main.models import Book
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(id=book_id)
    # Get or create a cart for the user (no 'is_active' filter)
    cart, created = Cart.objects.get_or_create(user=request.user)  # No is_active filter
    # Check if the book is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        # If the book is already in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')  # Redirect back to the cart page


@login_required
def cart_view(request):
    cart = Cart.objects.filter(user=request.user).first()  # Get the user's active cart
    
    if cart:
        # Fetch cart items
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            item.total_price = item.book.price * item.quantity  # Compute total price for each item
        
        # Calculate total cart price
        total_cart_price = sum(item.total_price for item in cart_items)

        # Fetch recommended books
        # Get categories of books in the cart
        cart_categories = set(item.book.category for item in cart_items)
        # Fetch other books from the same categories, excluding those already in the cart
        recommendations = Book.objects.filter(category__in=cart_categories).exclude(id__in=[item.book.id for item in cart_items])[:2]

        return render(request, 'cart/cart.html', {'cart_items': cart_items,'total_price': total_cart_price,'recommendations': recommendations})
    else:
        return render(request, 'cart/cart.html', {'cart_items': [],'total_price': 0,'recommendations': []})

    cart_items = CartItem.objects.filter(cart=cart)

    for item in cart_items:
        item.total_price = item.book.price * item.quantity  # Compute total price

    total_cart_price = sum(item.total_price for item in cart_items)

    # Get book categories in the cart
    cart_book_categories = [item.book.category for item in cart_items]
    
    # Fetch recommended books from the same category
    recommendations = Book.objects.filter(category__in=cart_book_categories).exclude(
        id__in=[item.book.id for item in cart_items]  # Exclude books already in the cart
    ).distinct()[:5]  # Limit to 5 recommendations for simplicity

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total_cart_price': total_cart_price,
        'recommendations': recommendations,  # Pass recommendations to the template
    })

@login_required
def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()

@login_required
def order_complete(request):
    # After clicking the "Buy" button, redirect to this view to show the success message
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    
    # Optional: Mark the cart as inactive or clear it
    cart.is_active = False  # Mark the cart as completed
    cart.save()
    # Delete cart items (or just leave them, depending on your workflow)
    cart_items.delete()

    return render(request, 'cart/order_complete.html')  # Redirect to the order complete page