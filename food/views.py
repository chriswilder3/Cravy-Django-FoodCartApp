from django.shortcuts import render
from django.http import HttpResponse

from .models import Item
from .forms import AddItemForm

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
    return render( request, 'item_details.html', context)

def add_item(request):
    if request.method == 'GET':
        # Remember we need to intiate the form here
        # then send it as context to the page
        form = AddItemForm()
        return render(request, 'add_item.html', {'form': form})