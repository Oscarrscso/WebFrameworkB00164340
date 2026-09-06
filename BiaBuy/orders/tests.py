from django.test import TestCase
from django.contrib.auth.models import User, Group
from .models import Order
# Create your tests here.
class OrderTests(TestCase):
    
    def test_request_refund(self):
        user = User.objects.create_user(username="user1", password="password")
        order = Order.objects.create(user=user)
        
        self.client.login(username="user1", password="password")
        self.client.post("/orders/return/" + str(order.id) + "/")

        order = Order.objects.get(id=order.id)
        self.assertEqual(order.status, "Refund Requested")

    def test_staff_refund(self):
        user = User.objects.create_user(username="user1", password="password")
        staff = User.objects.create_user(username="user2", password="password")
        group = Group.objects.create(name="Staff")
        staff.groups.add(group)
        order = Order.objects.create(user=user, status="Refund Requested")

        self.client.login(username="user2", password="password")
        self.client.post("/orders/refund/", {"order_id": order.id})

        order = Order.objects.get(id=order.id)
        self.assertEqual(order.status, "Refunded")
