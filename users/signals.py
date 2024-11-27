# Here We trying to build a signal such that, when user registration form
# is submitted, a profile is also automatically created for that user.

# Django includes a “signal dispatcher” which helps decoupled applications 
# get notified when actions occur elsewhere in the framework. 
# In a nutshell, signals allow certain senders to notify a set of 
# receivers that some action has taken place.

#  django.db.models.signals module defines a set of signals sent by 
# the model system

# Signals can make your code harder to maintain. Consider implementing
# a helper method on a custom manager, to both update your models and
# perform additional logic, or else overriding model methods before using
# model signals

# Model signals are sent by various model methods like __init__() or save()
# that you can override in your own code.
# For save(), there pre_save or post_save signals

from django.db.models.signals import post_save
# We want to create the profile after the form.save() is executed, 
# which internally would have called the model.save() also. 
# Hence post_save is used here

from django.contrib.auth.models import User
# we need the model which triggers it


# There are two ways of defining a receiver of the signal.
# 1. use connect method
#     from django.core.signals import request_finished
#     request_finished.connect(my_callback)
# 2. Use a receiver decorator
#     @receiver(signal, **kwargs)    

from django.dispatch import receiver
# This is a decorator that is directly applied on code(function), to 
# make it as a receiver of the signal.
# https://docs.djangoproject.com/en/5.1/topics/signals/#connecting-receiver-functions


# Some signals get sent many times, but you’ll only be interested in 
# receiving a certain subset of those signals. For ex:
# post_save sends signals everytime any instance of any model is saved.
# But we interested in one single model only, Hence we specify the sender of
# the signal here is User model.

# General syntax : 
# @receiver(signal= post_save, sender=Model_name)
# def my_handler(sender, **kwargs):
#     some_code..

# Note that **kwargs means, for this handler function, there may be
# multiple params sent by the sender. 1st argument to handler is always sender.
# But starting from second, We can receive any params that is avialable from
# sender by mentioning them first, and keep the rest as **kwargs
# Ex : post_save signal comes with many params, lets assume we want instance 
# only. We can say now
# def my_hanlder( sender, instance, **kwargs): 

from .models import Profile
# obviously we need this.

# First of all note that, Profile has same fields as User except 2 additional
# fields which are optional location and image ( filled null and default)
# Hence, the instance of User model (which gets saved after registerform is 
# saved) is passed here so that correspnding Profile can be generated.
#  We can worry about optional fields later.

@receiver( post_save, sender = User)
def build_profile( sender, instance, created, **kwargs):
    # Here instance is the instance of User just saved ,
    # created is a bool to indicate whether the model was saved 
    # correctly. **kwargs are any extra params. 
    if created:
        Profile.objects.create(user = instance)
        # If User instance was being created for first time, 
        # Use that instance to create a new instance(row)
        #  of profile also.

    # This ensures that the Profile table is always populated in sync with
    # the User table.

# Note that the above def is called only when the instance of User
# is created for the first time. But what should happen, when there are
# modifications done to the User table? corresponding Profile table
# must also be changed right?

# Hence Whenever any instance of User gets saved (after initial creation)
# We must save the corresponding profile instance corresponding to that User
# instance. 
# But note that, to access profile of a user that already created,
# We can call user.profile like before, but here instance.profile instead.
# Hence Lets create a receiver which does instance.profile.save() also.

@receiver( post_save, sender = User)
def save_profile( sender, instance, created, **kwargs):
    instance.profile.save()

# Work is not over yet. We still need to include these callbacks in the
# ready funcn of AppConfig in apps.py

# Since signals are sent to all receivers on every trigger, Why doesn't
# build_profile create issues even when we just made changes to existing 
# user? 
# The 'created' bool ensures that the Profile is only created if the 
# User instance is being created for the first time, not on subsequent saves.

# Technically We can combine them into one using IF-ELSE statements,
# but this is more cleaner. Since Signals are complicated, simplicity is IMP.

# Note : parameters for these functions are being passed by Django's signal 
# framework when post_save is triggered.



# Here are all the arguments sent along with post_save signal when its triggered

# sender
# The model class.

# instance
# The actual instance being saved.

# created
# A boolean; True if a new record was created.

# raw
# A boolean; True if the model is saved exactly as presented (i.e. when loading a fixture). One should not query/modify other records in the database as the database might not be in a consistent state yet.

# using
# The database alias being used.


# Signals VS Callbacks Terminology :

# Note that triggers like pre_save, post_save etc are 'signals' 
# The functions we write that receive them are 'callbacks' or 'signal handlers'
# The events or models that trigger them are called 'senders'