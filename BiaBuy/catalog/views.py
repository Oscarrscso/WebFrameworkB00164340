from django.shortcuts import render
from .models import Item

def catalog_page_sorted(request):
    sorted_catalog = Item.objects.order_by("-item_price")
    context = {"sorted_catalog": sorted_catalog}
    return render(request, "catalog/index.html", context)

def item_page(request, item_name_url):
    item = Item.objects.get(item_name=item_name_url)
    context = {"item": item}
    return render(request, "catalog/item_page.html", context)

