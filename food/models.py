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

    # Note that We need to modify add_item form, so that it will automatically
    # submit the user who added it, to this posted_by.

    # Remember, When including image/media ie, When handling file uploads 
    # the form must include the attribute enctype="multipart/form-data".
    # Without it, the uploaded file won't be included in the request.

    def __str__(self):
        return f" {self.name}"


