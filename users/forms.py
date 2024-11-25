from django.contrib.auth.forms import UserCreationForm

# Note that the form which we created in signup view, is default
# and may not include all the field we want to have.
# Hence can create our own form class and inherit from UserCreationForm
# and extend by adding our own fields etc

# Also to access and implement auth methods for users, we will 
# import User from contrib.auth
from django.contrib.auth.models import User
# Why we need this? Note that, while extending forms, we define
# meta class inside them that takes 2 things, model and fields.
# Now since we still dont have our own model of user(yet), we
# can use the User model from auth.models.
# Note that this User model also has limited fields. If we were 
# to include such uncommon fields associated with users
# ( ex :profile image, descritipn, salary etc). We will need to 
# provide our own models.

# And finally we need forms variable of django to create 
# custom form fields
from django import forms

class RegisterForm( UserCreationForm):
    # Define here, extra custom fields , NOT inside the parent class
    email = forms.EmailField()

    class Meta:
        model = User
        # Define here all the fields to be included in the form
        # including ones in base class and the extra ones we added
        fields = ['username', 'email', 'password1', 'password2']