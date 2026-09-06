from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order, OrderItem

# Create your views here.
def orders(request):
    if request.user.is_authenticated:

        is_staff = request.user.groups.filter(name="Staff") or request.user.groups.filter(name="Manager")
        if is_staff: #shows either every order if staff
            user_orders = Order.objects.all().order_by("-date_created")
        else: # or just users if customer
            user_orders = Order.objects.filter(user=request.user).order_by("-date_created")


        #calculate each items total and add to order total
        for order in user_orders:
            order.order_items = OrderItem.objects.filter(order=order)
            order.order_total = 0

            for order_item in order.order_items:
                order_item.item_total = order_item.item_price * order_item.quantity
                order.order_total += order_item.item_total
        context = {"user_orders": user_orders, "is_staff": is_staff}

        return render(request, "orders/index.html", context)
    else:
        return redirect("login")


def place_order(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            cart_items = CartItem.objects.filter(cart__user=request.user)
            if cart_items:
                new_order = Order.objects.create(user=request.user)
                for cart_item in cart_items:
                    OrderItem.objects.create(
                        order=new_order, 
                        item=cart_item.item,
                        item_name=cart_item.item.item_name,
                        item_price=cart_item.item.item_price,
                        quantity=cart_item.quantity,
                        )       
            
            cart_items.delete()

            return redirect("orders")
        return redirect("cart")
    else:
        return redirect("login")


def order_return(request, order_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            order = Order.objects.get(id=order_id, user=request.user)
            order.status = "Refund Requested"
            order.save()

        return redirect("orders")
    else:
        return redirect("login")


def manage_returns(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name="Staff") or request.user.groups.filter(name="Manager"):
            if request.method == "POST":
                order = Order.objects.get(id=request.POST["order_id"])
                order.status = "Refunded"
                order.save()

        return redirect("orders")
    else:
        return redirect("login")