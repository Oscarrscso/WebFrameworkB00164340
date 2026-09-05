from django.shortcuts import render, redirect
from catalog.models import Item
from .models import Cart, CartItem

# Create your views here.
def cart(request):
    user_cart = CartItem.objects.filter(cart__user=request.user)
    context = {"user_cart": user_cart}
    return render(request, "cart/index.html", context)

def add_to_cart(request, item_id):
    if request.method == "POST":
        item = Item.objects.get(id=item_id)

        user_cart = Cart.objects.filter(user=request.user)
        if user_cart:
             cart = user_cart.get()
        else:
            cart = Cart.objects.create(user=request.user)
        item_in_cart = CartItem.objects.filter(item=item, cart=cart)
        if item_in_cart:
            cart_item = item_in_cart.get()
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(cart=cart, item=item)
    return redirect("catalog_page_sorted")

def remove_from_cart(request, cart_item_id):
    if request.method == "POST":
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
    return redirect("cart")
