from django.http import HttpResponse
from .models import Item

def index(request):
    catalog = Item.objects.all()
    output = ", ".join([Item.item_name for Item in catalog])
    return HttpResponse(output)

def product(request, item_name):
    return HttpResponse("Product: %s\n Description: %s\n Price: %s" % item_name, item_desc)