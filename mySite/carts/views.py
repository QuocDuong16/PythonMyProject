from re import U
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from cinema.models import Movie
from carts.models import Cart, CartItem
from django.contrib import messages
# Create your views here.

def add_cart(request, movie_id):
    current_user = request.user
    movie = Movie.objects.get(id=movie_id)  # Get object product
    if current_user.is_authenticated:
        if request.method == 'POST':
            print("Invalid")
        cart = Cart.objects.get(user=current_user)
        is_exists_cart_item = CartItem.objects.filter(movie=movie, cart=cart).exists()
        if is_exists_cart_item:
            messages.error(request=request, message="Vé này đã được mua")
        else:
            cart_item = CartItem(
                movie=movie,
                cart=cart,
                quantity=1
            )
            cart_item.save()
        return redirect('cart')
    else:
        messages.error(request=request, message="Chưa đăng nhập")
        return redirect('cart')

def remove_cart_item(request, movie_id, cart_item_id):
    movie = get_object_or_404(Movie, id=movie_id)
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cart_item = CartItem.objects.get(
                id=cart_item_id,
                movie=movie,
                cart=cart,
            )
            cart_item.delete()
    except Exception:
        pass
    return redirect('cart')

def cart(request, total=0, cart_items=None):
    if request.user.is_authenticated:
        check = True
        user = 'Hello ' + request.user.username
        if request.user.is_superadmin == False:
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            for cart_item in cart_items:
                total += cart_item.movie.ticket_fare
            tax = total * 5 / 100
            grand_total = total + tax
    else:
        check = False
        user = ""
    context = {
        'check': check,
        'user': user,
        'total': total,
        'cart_items': cart_items,
        'tax': tax if "tax" in locals() else "",
        'grand_total': grand_total if "tax" in locals() else 0,
    }
    return render(request, 'cart/cart.html', context=context)

def checkout(request):
    return render(request, 'cart/checkout.html')
