from django.contrib import admin
from django.urls import path, include  # Import the include function
from zomato import views  # Import the views module from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the app's URL patterns using the include function
    path('', include('zomato.urls')),
]
