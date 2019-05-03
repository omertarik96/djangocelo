# UH CELO with Django backend

This repo aims to replicate [UH CELO](https://dev.azure.com/celocsuh/CELO) and add more functionality using Python Django Framework.

# Current Views

## Student Dashboard

[student-dashboard-view](https://i.imgur.com/14Lmdrb.png)

# Instructions

Make sure that you have Python3.6 installed in your computer. If not install it from [here](https://www.python.org/)

First you need to clone the repo using this command:

``git clone https://github.com/omertarik96/djangocelo``

``cd djangocelo``


After that please install all required dependencies.

``pip install -r requirements.txt`` 

Run the migrations for the database.

``python manage.py makemigrations``

``python manage.py migrate``

Create the super user. This user will be the admin for your local development.

``python manage.py createsuperuser ``

After running this command it will ask for username, password.

Run the server on localhost.

``python manage.py runserver``

You can access the site using following URLs:

Frontend: ``localhost:8000/``

Admin Panel:``localhost:8000/admin/`` 