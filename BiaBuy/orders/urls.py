from django.urls import path

from . import views

urlpatterns = [
    path("", views.orders, name="orders"),
    path("place/", views.place_order, name="place_order"),
]