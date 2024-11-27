from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length= 255)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'product_images/', null= True)

    # The below posted_by was added much later.
    # We want to display who added this item . Note that We
    # This person who added the item, must be a User also. 
    # Hence There is many to one correlation between Item and User.
    # and One-Many relations are defined by foreign Key. In Django
    # We directly link it with ForeginKey(), so that posted_by is 
    # always equal to id of the submitter in User model.

    posted_by = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    # Since there are some unlinked items in the DB, we will let 
    # them have posted_by as 1 for now.(user :admin )

    # Note that We need to modify add_item view, so that it will automatically
    # submit the user who added it, to this posted_by.

# -------------------------------------------------

    # For many functions such as redirecting to item_details page
    # after item has been added, We need to get the Abs. URL 
    # of the item_details, but dynamically.
    # For this We will implement a method for this Item model.
    # The Django Model has method called  get_absolute_url which can 
    # be extended to specify a way to get abs. URL.
    def get_absolute_url(self):
        return reverse("food:item_details", kwargs = {'pk':self.pk})

    # reverse() is used to generate a URL based on the name of a view 
    # in your urlpatterns. It replaces the need to hardcode URLs and 
    # ensures that if you change the URL pattern later, the function will
    #  still generate the correct URL.

    # kwargs provides the arguments required to generate the URL.
    # In this case, pk (primary key) is used in the item_details URL pattern
    # eturns the generated URL as a string. EX: if the pk of the item is 42,
    #  the function will return : /item_details/42/

    # So now, to get the URL of detail page of any item , We can call this 
    # method directly on the item instance. Ex : item.get_absolute_url()

    # How is it Used?
    #  After saving or modifying an object, you can redirect to its detail page:
    #     def add_item(request):
    #         new_item = Item.objects.create(name="Example")
    #         return redirect(new_item.get_absolute_url())
    # When rendering an HTML page, you can use get_absolute_url to link to the detail view of an item:
    #    <a href="{{ item.get_absolute_url }}">View Details</a>
    
    # Why is it used?
    # You define the logic for generating URLs in one place, avoiding 
    # hardcoding the URL in multiple views or templates.
# ---------------------------------------------------

    # Remember, When including image/media ie, When handling file uploads 
    # the form must include the attribute enctype="multipart/form-data".
    # Without it, the uploaded file won't be included in the request.

    def __str__(self):
        return f" {self.name}"


