from django.shortcuts import render,redirect

# Instead of using custom forms, We can use UserCreationForm
# provided by django directly without needing to define models
# and forms for it. Just use it directly

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
# messages framework is used to display cookie or session based
# flash messages. Ex: After submitting form
# learn more here : https://docs.djangoproject.com/en/5.1/ref/contrib/messages/


# Create your views here.

def signup( request):
    if request.method == 'GET':
        form = UserCreationForm()
        # Be default the usercreationform has 3 fields
        # username, password1 and password2
        return render( request, 'signup.html', {'form':form})
    else:
        form = UserCreationForm( request.POST)
        if form.is_valid():
            # Now that the form is valid, We will display a success message
            # The messages framework allows us to temporarily store 
            # messages in one request and retrieve them for display
            # in a subsequent request.

            # There are 5 levels of messages that can be put out as given below
            # Level : Tag

            # DEBUG debug
            # INFO  info
            # SUCCESS   success
            # WARNING   warning
            # ERROR    error

            # We can add above type of message using add_message() by passing
            # request object, message tag, and actual message string to it

            # messages.add_message(request, messages.INFO, 'Our app is cool')

            # OR we can use shortcuts provided for each type of message tags
            # Ex : messages.info(request, 'And you know it! ')

            # So now lets produce a message of succes tag.(since form was success)
            # But first lets extract username, that we can include it in
            # success message.

            username = form.cleaned_data['username']
            messages.success( request, f' Welcome {username}, Registration was successful')
            # The work is still NOT done. We need to display the actual message
            # in the template themselves. Note that since messages are 
            # attached to request/cookie sessions and built using context_processors
            # they are available throughout the session in every template/url.
            # But We will display it in master.html below navbar since that displays
            # it any page we go to after form submit.


            form.save() 
            # Note: Just like any other form, its necessarty to save
            # the usercontent form also
            return redirect('food:home')
        else:
            return render(request, 'signup.html', {'form': form})
