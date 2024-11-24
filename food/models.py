from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length= 255)
    description = models.CharField(max_length= 255)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'product_images/', null= True)

    # Remember, When including image/media ie, When handling file uploads 
    # the form must include the attribute enctype="multipart/form-data".
    # Without it, the uploaded file won't be included in the request.

    def __str__(self):
        return f" {self.name}"


