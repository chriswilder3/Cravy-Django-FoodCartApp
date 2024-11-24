from django import forms # Provides classes and methods for
                        # handling forms

from .models import Item

class AddItemForm( forms.ModelForm):
    # ModelForm is a baseclass, that can create forms based on Django models
    # It creates form fields based on the model field types

    class Meta:
        # Meta class provides necessary meta information to the 
        # ModelForm. It is where model and fields to be included
        # in the form are declared.

        model = Item 
        fields = ['name','description','price','image']
        

