## Intro to Django

### Reading

- Web Development with Django, CH. 1
- https://www.w3schools.com/django/index.php

### Learning Outcomes

- What is Django
- Django install & app creation
- Django app structure
- Django urls & views

### Whaat is Django

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

