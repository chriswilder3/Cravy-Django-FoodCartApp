from django.shortcuts import render,redirect
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
    else:
        
        # Lets create a new instance of the form from the
        # fields provided through input 
        # But note that when media/files are sent through POST
        # data comes through 2 parts. first contains other fields and
        # metadata. second contains the files, Which are stored in
        # FILES variable of request object
        # Hence we need to acess text fields through request.POST
        # and media/files through request.FILES
        # And when we instantiate the form we need to pass both
        # of these variables.
        form = AddItemForm( request.POST, request.FILES)

        if form.is_valid():
            # Unlike custom forms, model forms save the data to model 
            # directly
            form.save()
            return redirect('/')
        else:
            print(form.errors)
            # Now dont redirect because it will just create
            # new instance of form that doesnt hold errors of this instance
            # Hence render the template again, but with this instance
            # of form passed

            return render(request, 'add_item.html', {'form':form})
