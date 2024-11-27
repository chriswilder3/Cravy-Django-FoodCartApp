from django.urls import path
from . import views

app_name = 'food' # This is used to refer to names of paths 
                 # in combination with it, to avoid conflicts with
                 # possible same names from other apps.

                 # We can refer the names now as food.name_of_url_pattern
                 # in the template. Ex :{% url 'food:item' %}
                 # Remember its :(colon) not .

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.IndexListView.as_view(), name='home'), # custom class view 

    # path('item_details/<int:id>', views.item_details, name='item_details'),
    path('item_details/<int:pk>', views.FoodDetails.as_view(), name='item_details'),
    # path('item/add', views.add_item, name='add_item'),
    path('item/add', views.CreateItem.as_view(), name='add_item'),

    path('item/update_item/<int:id>', views.update_item, name='update_item'),
    path('item/delete_item/<int:id>', views.delete_item, name='delete_item'),
]

# since we have defined get_absolute_url for the Item model,
# as soon as we submit the additem form, we are redirected to
# that item's detail page since it works internally to resolve the 
# URL needed to do this by using get_absolute_url.