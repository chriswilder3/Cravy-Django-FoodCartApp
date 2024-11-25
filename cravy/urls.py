"""
URL configuration for cravy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
    # The configurations defined in settings.py are available
    # in this module. Ex: MEDIA_URL, STATIC_ROOT etc

from django.conf.urls.static import static
    # static function is a tool provided by django to serve
    # static and media files during DEVELOPMENT.
    # As we know, the media_root is where media files are 
    # stored. When user requests for these images/media,it happens
    # through URLs, ex : src attr of img tag. Now 
    # static function is used to append additional
    # URL patterns of media access just like path() does.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')),
    path('users/', include('users.urls'))
]

if settings.DEBUG:
    # Note that this configuration of serving media files by django
    # itself is active during development. While deployed, the
    # servers like apache or nginx themselves serve files from file system.

    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    # As we might notice, the function is very similar to path()
    # defined in urlpatterns at top. Because it works same way.
    # Whenever user requests for media with given url = MEDIA_URL
    # The path corresponding to that media is served , so 
    # That the media is displayed back to user/template.
