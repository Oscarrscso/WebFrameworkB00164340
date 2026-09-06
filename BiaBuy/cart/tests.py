from django.test import TestCase
from django.contrib.auth.models import User
from catalog.models import Category, Item
from .models import Cart, CartItem
# Create your tests here.

class CartTests(TestCase):
    def test_add_to_cart(self):
        user = User.objects.create_user(username="user1", password="password")
        cart = Cart.objects.create(user=user)
        category = Category.objects.create(category_name="Fruit")

        item = Item.objects.create(
        category=category,
        item_name="Apple",
        item_desc="red",
        item_price="0.30",
        )

        self.client.login(username="user1", password="password")
        self.client.post("/cart/add/" + str(item.id) + "/")

        cart_item = CartItem.objects.get(cart=cart, item=item)
        self.assertEqual(cart_item.quantity, 1)
