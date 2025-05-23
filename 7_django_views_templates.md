## Django Views & Templates

### Reading

- Web Development with Django, CH. 3
- https://www.w3schools.com/django/django_views.php
- https://docs.djangoproject.com/en/5.2/intro/tutorial03/
- https://docs.djangoproject.com/en/5.2/intro/tutorial06/

### Reference
- https://www.w3schools.com/django/django_urls.php
- https://www.w3schools.com/django/django_templates.php
- https://www.pluralsight.com/guides/introduction-to-django-views
- https://docs.djangoproject.com/en/5.2/#the-view-layer
- https://docs.djangoproject.com/en/5.2/#the-template-layer

### Learning Outcomes

- HTTP request handling with Django
- Function-based & Class-based views
- Complex HTML response with Django templates


### Django Views

Django Views take in a web request and provide a web response. The view contains application logic, such as interfacing with the database, and controls how data will be displayed.

Django views can be **function-based** or **class-based** views. 

Function-based views are implemented as Python functions. For example:
```python
    from django.http import HttpResponse

    def home_page(request):
        message = "<html><h1>Welcome to my Website</h1></html>"
        return HttpResponse(message)
```

Views automatically receive the HTTP request as the first input parameter and can customize the response based on it's contents. For example:

```python
    def home_page(request):
        name = request.GET.get("user_name", "Stranger") # default to Stranger if no user_name provided
        message = f"<html><h1>Welcome {name} to my Website</h1></html>"
        return HttpResponse(message)
```


Class-based views are implemented as Python classes that inherit from Django's generic view classes and have various pre-built properties and methods to simplify view operations.

We'll cover class-based in depth a bit later.


### Django URLs

Django's URL configuration maps incoming requests to the appropriate view function for processing. URL configuration is in a **urls.py** file like this:

    from . import views 
    urlpatterns = [
        path('', views.home, name='home'),
        path('url-path/' views.my_view, name='my-view'),
    ]

Where:
* **urlpatterns** is a list of URL paths
* the empty path corresponds to the site root
* **url-path** is a route or pattern to match. The pattern can be a regular expression.
* **my_view** is the view function (or class) to invoke

Parameters defined in the URL path are passed into the view for processing. For example, this pattern:

    urlpatterns = [
        path(r'^url-path/<int:id>/', views.my_view,   name='my-view')
    ]

would pass the integer value after `url-path/` into the view as a variable called `id`.

### Templates

By default, Django uses the `DjangoTemplates` engine and Django template language to render dynamic HTML content. Django can be configured to use other template engines, such as Jinja2.

Django looks for templates in a `templates` folder of each `application` (sub-folder) unless specified otherwise in the `TEMPLATES` configuration of `settings.py`. 

If your templates are in the main application folders, you'll need to tell Django to look there in settings.py, like this:

```commandline
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mysite/templates')],
```


Django views can `render` a template-based response back to the browser by specifying the template name and `context` variables for use by the template.

```python
from django.shortcuts import render

def home(request):
    name = request.GET.get('name', None)
    return render(request, 'index.html', {'name': name})
```


Django's template language syntax is similar to Jinja2 and uses double curly braces to identify variables that Django can replace with dynamic values:

    {{ variable }}

Django template language supports control flow logic as well:

    <ul>
        {% for element in element_list %}
            <li>{{ element.title }}</li>
        {% endfor %}
    </ul>

### Static Files
