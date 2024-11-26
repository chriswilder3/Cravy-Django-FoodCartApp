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

    # Accessing Profile Data in the view/shell:
    # user = User.objects.get(username="example_user")
    # profile = user.profile  # Access the related profile

    # Even though Profile is a separate model, the reason you 
    # can access it through user.profile is because of the OneToOneField
    #  relationship in Django, which establishes a reverse relationship
    #  between the two models.
    #  It allows us to navigate from the related model (User) back to 
    # the model containing the OneToOneField (Profile).

    # The reverse relationship (user.profile) is possible because Django
    #  dynamically adds this attribute(profile, by default) to the User 
    # model during runtime

    # This behavior is controlled by the related_name attribute of the 
    # OneToOneField. If you don’t specify related_name, Django uses the 
    # lowercase name of the related model (profile in this case) by default.

    location = models.TextField( null = True)

    profile_pic = models.ImageField( default ='profile.png', upload_to='profile_pics')

    def __str__(self):
        return f' {self.user.username}'

    # Overall, to access authuser fields username/email then 
    #       user.username, user.email is enough
    # But to access profile fields then 
    #       user.profile.image, user.profile.location are used.