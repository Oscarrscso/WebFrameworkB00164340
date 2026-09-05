from django.shortcuts import render, redirect
from catalog.models import Item
from .models import Cart, CartItem

# Create your views here.
def cart(request):
 if request.user.is_authenticated:
    user_cart = CartItem.objects.filter(cart__user=request.user)
    cart_total = 0

    for cart_item in user_cart:
        cart_item.item_total = cart_item.item.item_price * cart_item.quantity
        cart_total += cart_item.item_total

    context = {
                "user_cart": user_cart, 
                "cart_total": cart_total, 
               }
    return render(request, "cart/index.html", context)
 else:
    return redirect("login")

def add_to_cart(request, item_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            item = Item.objects.get(id=item_id)
            cart = Cart.objects.get(user=request.user)

            item_in_cart = CartItem.objects.filter(item=item, cart=cart)
            if item_in_cart:
                cart_item = item_in_cart.get()
                cart_item.quantity += 1
                cart_item.save()
            else:
                CartItem.objects.create(cart=cart, item=item)
        return redirect("catalog_page_sorted")
    else:
        return redirect("login")
    
def remove_from_cart(request, cart_item_id):
    if request.user.is_authenticated: 
        if request.method == "POST":
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.delete()
        return redirect("cart")
    else:
        return redirect("login")

def edit_cart_quantity(request, cart_item_id):
    if request.user.is_authenticated: 
        if request.method == "POST":
            new_quantity = int(request.POST["quantity"])

            if new_quantity > 0:
                cart_item = CartItem.objects.get(id=cart_item_id)
                cart_item.quantity = new_quantity
                cart_item.save()

        return redirect("cart")
    else:
            return redirect("login")