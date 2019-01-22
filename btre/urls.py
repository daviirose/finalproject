from django.contrib import admin
from django.urls import path, include

# Creates a path but also sends request to look inside the pages.urls file
urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
] 
