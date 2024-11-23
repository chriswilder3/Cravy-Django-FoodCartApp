from django.shortcuts import render
from django.http import HttpResponse

from.models import Item

# Create your views here.

def home(request):
    items = Item.objects.all()
    context = {
        'items':items,
    }
    # print(items.values())
    return render(request, 'index.html', context)

def item(request):
    return HttpResponse('Items')

def item_details( request, id):
    item = Item.objects.get(id =id)
    context = {
        'item':item,
    }
    render( request, 'item_details.html', context)
