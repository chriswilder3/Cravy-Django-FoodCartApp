from django.apps import AppConfig

# IMP : In your app directory, make sure to update the __init__.py to 
# use the new AppConfig.

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # the AppConfig class is used to configure some of the attributes of
    # the application.
    # The ready method in Django's AppConfig class is used for
    # initializing the app when it's ready to start. This method 
    # allows you to execute code that should run once the application 
    # is fully loaded and all models are available.
    
    # It's useful for tasks like: Signal Registration
    # Ensuring that signal handlers(callbacks) are registered making sure your 
    # signals are connected and ready to respond when specific events occur

    def ready(self):
        # Hence lets register our signal callbacks here
        # Again what it means is we are simply importing those callbacks
        # here so that they are ready to connect to signals and work 
        # as soon as app starts.
        import users.signals    

