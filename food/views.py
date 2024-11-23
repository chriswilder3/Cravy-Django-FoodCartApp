from django.shortcuts import render
from django.http import HttpResponse

from.models import Item

# Create your views here.

def home(request):
    items = Item.objects.all()
    context = {
        'items':items,
    }
    return render(request, 'index.html', context)

def item(request):
    return HttpResponse('Items')
