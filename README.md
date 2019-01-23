# RealEstate Application
This app will be created in Django/Python.

# Overview
For my third/fourth semester of the Software Development program at Thaddeus Stevens College of Technology, I will be buidling a dynamic web application for a fictional company named btre. I will document how I approached every issue I come accross, and the full process until the finish product. 


# Requirements
1. Create a database with tables to store your data structure
2. Create a well structured web interface and backend api to power your project
3. Frontend component
4. Backend component
5. Administration Portal
6. Data Analysis & visualizations
7. API Implementation
8. Data Architecture

# The Process:
After creating a folder and a file for my new project I proceed to my next step which was creating virtual environment. The purpose of this is to keep certain packages and dependencies isolated inside of your project rather than in a global scope. You would want what will benefit your project not extra dependencies and packages you don’t really need.

### Creating a Virtual Environment
		
    python3 –m venv ./venv
	
### Activate Environment 

    source ./venv/bin/activate

### Leaving Environment
	
    Deactivate

I just created my virtual environment, I made sure I was inside the virtual environment in order to install Django which is a python framework inside the environment and not globally.

### Installing Django
    
    pip install Django

### Gitignore

Django will want to ignore specific files inside your project.
Visit gitignore.io for a default version of a gitignore within Django.

### Starting Project in Django

    django-admin startproject  btre .

• Btre: Project name

### Creating The Pages App

    python manage.py startapp pages 

/* Add your mini apps into your settings.py in the btre folder (Root of project) */

### Formatters
You might get an error involving formatters espcially if you are using VSCode. It might ask you to install it through VSCode but this will only do it globally, you want it inside your virtual environment instead.

Inside your venv run this command: pip install autopep8

### Outputting Templates/Linking URLS

First I have to tell Django where to look for the templates. In the root of the Django project which is my BTRE folder go to settings.py, onto the templates list and give the directory a path. It would look something like this:
'DIRS': [os.path.join(BASE_DIR, 'templates')],

• BASE_DIR just means the root directory

• Templates defines the folder name

### Linking URLS/VIEWS.py
The proper way to link your URL files:

    path('about', views.about, name='about') This is simply looking for the file 'About' inside your views.py

The proper way to link your Views files:

    def about(request):
        return render(request, 'pages/about.html')

Note: This simply sends out a request to look inside the 'pages(folder)/about.html(Frontend)'

Note: since the BASE_DIR has a path towards the templates folder it will know to look inside the right pages folder.

### Static Folder
Create a Statics folder inside the generated BTRE folder. The BTRE folder was genertaed when we ran startproject.
Inside the Static folder add:

• img folder
• js folder
• css folder

In settings.py of root project add:


    STATIC_ROOT= os.path.join(BASE_DIR, 'static')

And 

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'btre/static')
    ]

When you deploy your app you run a command called 'collectstatic' and it goes into all your apps. If it has a static folder it takes everything out and puts it into a root static folder. Thats what im defining here.

Run the command: 
    
    python manage.py collectstatic

This will find any static folder I have, collect it, create one into as whatever I define the Static root name which is static. When I deploy this is the folder it will look for and not the root 'static' folder.
