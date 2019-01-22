from django.urls import path

from . import views # From All import views

# Route that tells it to look for index and about in the views file
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]