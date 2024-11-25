from django.urls import path
from . import views

app_name = 'food' # This is used to refer to names of paths 
                 # in combination with it, to avoid conflicts with
                 # possible same names from other apps.

                 # We can refer the names now as food.name_of_url_pattern
                 # in the template. Ex :{% url 'food:item' %}
                 # Remember its :(colon) not .

urlpatterns = [
    path('', views.home, name='home'),
    path('item/', views.item, name = 'item'),
    path('item_details/<int:id>', views.item_details, name='item_details'),
    path('item/add', views.add_item, name='add_item'),
    path('item/update_item/<int:id>', views.update_item, name='update_item'),

]