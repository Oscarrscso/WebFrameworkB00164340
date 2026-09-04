from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:item_name>/", views.product, name="product"),
]