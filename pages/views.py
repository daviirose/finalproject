from django.shortcuts import render
from django.http import HttpResponse

# Sends out a request to look inside the templates/pages folder for our html files
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')