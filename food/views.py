from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Item
from .forms import AddItemForm

from django.views.generic.list import ListView
# We will be creating classbased ListView.

# Create your views here.

def home(request):
    items = Item.objects.all()
    context = {
        'items':items,
    }
    # print(items.values())
    return render(request, 'index.html', context)

# Here we will implement a class based view, for demo. Note that class based
# views workflow is similar to function views : urls -> views ->models
# -> templates. We already used 2 class views : LoginView/ LogoutView.
# But they have some differences and advantages compared to function views.
# learn later : https://docs.djangoproject.com/en/5.1/topics/class-based-views/

# For now must read this : https://docs.djangoproject.com/en/5.1/topics/class-based-views/intro/#using-class-based-views
# We will be implementing generic class views: https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/#built-in-class-based-generic-views
# After reading prev doc, we know that ListView help generate list views of objects
# Since home funcn view does the same thing, Lets create ListView for it.

class IndexListView(ListView):
    model = Item  # Model from which the view fetches objects to show as list
    template_name ='index.html' # which template to use to display this list.
    context_object_name = 'items' # If we dont specify this django will
        # assume object_list var is default name, tries to render like that
        # in the template. But in index.html we used {{items}}.Hence 
        # context_object_name needs to be changed (for our temlates atleast)

    # Note that Above attr.s are properites of python class and its not 
    # necessary we specify them here, in urls.py we can specify them inside
    # .as_view() method also. Rememeber LoginView/LogoutView in users.
    # Anyway now lets go to url.py(of food) to route home requests to this view.
    # Tested : It works fine. Lets add class based detailview for below funcn also.


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
        return render(request, 'add_item.html', {'form': form, 'update':False})
        # Look at the update_item view to know more about update flag.
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

            return render(request, 'add_item.html', {'form':form, 'update':False})


def update_item( request, id):
    item = Item.objects.get( id = id)
    # We need to get the model instance correspondng to
    # the item we want to update. Why?
    # Because, while instantiating the form, now this instance
    # must be passed along with form to populate it.

    # Note that we will use exisisting AddItemForm again here. But
    # This item it will be prepopulated and when submitted will 
    # give data to this view.

    # But first, in the itemdetail page, Lets say we click on update item
    # button. Then we need to be redirected to add_item.html template
    # but it must be a GET request( when we first go to form page
    # we are asking to render the form only not accept inputs )
    # and url must be associated with this view.
    # EX : item/update_item/id
    # When this get request is received, this view should instantiate
    # the AddItemForm, but it should pass instance of the food
    # for which update button was clicked. ie, the 'item' variable above

    if request.method == 'GET':
        form = AddItemForm( instance = item)
            # The instance=item argument is used to bind the form to the
            # specific item for both prepopulating the fields (in GET) and 
            # saving the updated data (in POST).

            # Note that both form and item instance must be passed as
            # context here since item will used later for prepopulating.

            # We will also pass an update flag to add_item.html template
            # so that depending whether its additem/ updateitem operation,
            #  headings can be changed there.

        context ={
            'form':form,
            'item':item,
            'update': True,
        }
        return render(request, 'add_item.html',context)

    else:
        form = AddItemForm( request.POST, request.FILES, instance = item)
        # Why instance is also being passed when its POST request
        # which means form has been already submitted by this point?
        # THis is because, it tells the form which model instance to
        # to update specifically. If instance is not passed, the form
        # will create entirely new instace(new row in DB) instead of
        # updating an existing one.

        if form.is_valid():
            form.save()
            return redirect('/')
        
        else:
            # It form is not successful, again we need to render the 
            # the additem template but with current instance of form passed.
            context = {
                'form':form,
                'item':item,
                'update': True,
            }
            return render( request, 'add_item.html', context)

def delete_item( request, id):
    item = Item.objects.get( id=id)
    item.delete()
    return redirect('food:home')
