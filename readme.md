If you are a granted access to 139.147.9.242 (Lafayette College)

Create SSH tunnel:
- Open a new terminal window
- Type: ssh -L 3333:127.0.0.1:5432 youremail@139.147.9.242 -N 
- Keep the terminal open or connection to DB will be lost!

If you are not

In settings.py, change the database settings to your preferred DB.
Use the CSV files necessary in the csv_data.zip file to create the necessary relations.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'soccer',
        'USER': '<root>',
        'PASSWORD': '<password>',
        'HOST': 'localhost',
        'PORT': 3333,
    }
}

Aside from the official Django documentation (https://docs.djangoproject.com/en/3.0/), we have found this tutorial to be useful in setting up Django (https://tutorial.djangogirls.org/en).