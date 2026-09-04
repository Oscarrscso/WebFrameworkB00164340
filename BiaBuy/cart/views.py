from django.shortcuts import render
from catalog.models import Item


# Create your views here.
def cart(request):
    return render(request, "cart/index.html", {})