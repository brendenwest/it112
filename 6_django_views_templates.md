## Django Views & Templates

### Reading

- Web Development with Django, CH. 3
- https://www.w3schools.com/django/django_views.php

### Reference
- https://www.w3schools.com/django/django_urls.php
- https://www.w3schools.com/django/django_templates.php
- https://www.pluralsight.com/guides/introduction-to-django-views
- https://docs.djangoproject.com/en/4.1/topics/http/views/

### Learning Outcomes

- HTTP request handling with Django
- Function-based & Class-based views
- Complex HTML response with Django templates


### Django Views

Django Views take in a web request and provide a web response. The view contains application logic, such as interfacing with the database, and controls how data will be displayed.

Django views can be **function-based** or **class-based** views. 

Function-based views are implemented as Python functions. For example:

    from django.http import HttpResponse

    def home_page(request):
        message = "<html><h1>Welcome to my Website</h1></html>"
        return HttpResponse(message)

Class-based views are implemented as Python classes that inherit from Django's generic view classes and have various pre-built properties and methods to simplify view operations.

For example, to render an HTML page without any database interaction:

    from django.views.generic import TemplateView
    
    class HomePage(TemplateView): 
        template_name = 'home_page.html'

### Django URLs

Django's URL configuration routes incoming requests to the appropriate view function for processing. URL configuration is in a **urls.py** file like this:

    from . import views 
    urlpatterns = [path('url-path/' views.my_view, name='my-view'),]

Where 
* **urlpatterns** is a list of URL paths
* **url-path** is a route or pattern to match. The pattern can be a regular expression.
* **my_view** is the view function (or class) to invoke

Parameters from the URL path can be passed into the view for processing. For example, this pattern:

    urlpatterns = [
        path(r'^url-path/<int:id>/', views.my_view,   name='my-view')
    ]

would pass the integer value after `url-path/` into the view as a variable called `id`.

### Templates

By default, Django uses the `DjangoTemplates` engine and Django template language to render dynamic HTML content. Django can be configured to use other template engines, such as Jinja2.

Django applications can specify a templates folder in the `TEMPLATES` configuration of `settings.py`. For example:

    TEMPLATES = \
    
    [{'BACKEND': 'django.template.backends.django.DjangoTemplates',\
    
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ...

Django's template language syntax is similar to Jinja2 and uses double curly braces to identify variables that Django can replace with dynamic values:

    {{ variable }}

Django template language supports control flow logic as well:

    <ul>
        {% for element in element_list %}
            <li>{{ element.title }}</li>
        {% endfor %}
    </ul>