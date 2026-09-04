from django.urls import path

from . import views

urlpatterns = [
    path("", views.catalog_page_sorted, name="catalog_page_sorted"),
    path("<str:item_name_url>/", views.item_page, name="item_page"),
]