from django.db import models

from django.contrib.auth.models import User
# In addition to default authuser model(which gets filled through
# RegisterForm), We also need a model to store other user information
# such as profile pic, address etc

# Instead of modifying the default User model directly 
# (which can lead to compatibility issues), it's a best practice to 
# create a separate Profile model and link it to the User model.

# We will create such custom model, then we are going to issue a
# one to one association with auth.User model

# Create your models here.

class Profile( models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    #  The user field establishes a one-to-one link with the User model,
    #  ensuring each Profile is associated with exactly one User instance.
    # It ensures that each user can have only one associated Profile, 
    # and vice versa.

    # So now we can access the fields of User : username and email (not password though)
    # using prof_object.user.username/ prof_object.user.email anywhere

    location = models.TextField( null = True)

    profile_pic = models.ImageField( default ='profile.png', upload_to='profile_pics')

    def __str__(self):
        return f' {self.user.username}'