from django.urls import path
from . import views

from django.contrib.auth import views as AuthViews
# for login and logout instead of using custom views, We are going to
# use much better secure way. We will use built in view provided by 
# Django's auth package. These only need a template to render.
# learn more : https://docs.djangoproject.com/en/5.1/topics/auth/default/#all-authentication-views

# Since all authviews are class views, we need to call them in url patterns
# using their method as_view(), For Ex : LoginView.as_view()
# few imp params to it are : 
# 1. template_name : path to the template associated with these auth views. 
# 2. next_page : URL to which to redirect after login ( We can permanently
#           set this up in setting.py with LOGIN_REDIRECT_URL)
# 3. form : A modified authentication form (if necessary) and so on...........

# Note that these views, behave the same way we wrote our other forms. 
# ie, GET and POST are handled accordingly and form with error is also
# passed with refresh if validation fails. In the template, We can include
# 2 fields which are default given in forms of loginView,
# username and password only. 

# Again Note that our work is not yet done. Even though the form will show up
# and login , after login django tries to go to accnt profile url that is predefined (/account/profile)
# We need to change this to go to page of our choice.
# For now we will set LOGIN_REDIRECT_URL in the settings.py

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    path('login/', AuthViews.LoginView.as_view( 
        template_name ='login.html'), name='login'),
    
    path('logout/', AuthViews.LogoutView.as_view( 
        template_name ='logout.html'), name= 'logout' ),
        # Here note that logoutview also handles only post request like
        # a form( which is weird).So make sure to put the logout button
        # inside a form post

    path('profile/', views.profile, name='profile'),
]

