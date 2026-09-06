from django.urls import path

from . import views

urlpatterns = [
    path("", views.orders, name="orders"),
    path("place/", views.place_order, name="place_order"),
    path("return/<int:order_id>/", views.order_return, name="order_return"),
    path("refund/", views.manage_returns, name="manage_returns"),
]