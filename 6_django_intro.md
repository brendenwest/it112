## Intro to Django

### Reading

- Web Development with Django, CH. 1
- https://docs.djangoproject.com/en/5.2/intro/tutorial01/
- https://www.w3schools.com/django/index.php
- https://www.datacamp.com/tutorial/web-development-django

### Learning Outcomes

- What is Django
- Django install & app creation
- Django app structure
- Django urls & views

### What is Django

Django is a Python framework designed for building complex, data-driven web sites. It comes with built-in features like authentication, database integration (ORM), templating, administrative interface and much more.

Django follows the MVT design pattern (Model View Template).

#### Model

Defines a data object & usually maps to a database table.

Django models are usually located in a file named **models.py**.

#### View

Defines an HTTP request handler mapped to a URL. Returns content, often by fetching & transforming database data. 

Django views are usually contained in a file named **views.py**.

#### Template

A text file that defines a web page layout. Views can combine data & templates to generate an HTTP response. 

Django templates are usually located in a folder named **templates**.

#### Urls

Django maps urls (aka routes) to views in a file called **urls.py**.

### Installing Django

As with other Python projects, it's good practice to use a **virtual** environment if developing on your local pc.

Once you have the virtual environment activated, you can install Django like so:

Windows:
```commandline
(env) C:\Users\Your Name>py -m pip install Django
```

Unix/MacOS:
```commandline
(env) ... $ python -m pip install Django
```

### Creating a Django Project

All files for a Django project are contained within a single folder. You can create the folder and files by run this command (be sure to replace `my_project_name` with the appropriate name:

```commandline
django-admin startproject my_project_name
```

### Running the Django server

Navigate to the project folder you created in the previous step and run this command:

```commandline
py manage.py runserver
```

This will start the Django `server` (on port 8000 by default), which you can access via a browser at http:// 127.0.0.1:8000