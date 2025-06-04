## REST APIs w Django

### Reading

- Web Development with Django, CH. 12
- https://www.django-rest-framework.org/#quickstart
- https://www.freecodecamp.org/news/how-to-build-a-rest-api-in-django/

### Learning Outcomes

- Django JsonResponse
- Using Django Rest Framework
- Using serializers
- Applying permissions on API endpoints

### Django REST APIs

As discussed in a previous module, REST APIs are web endpoints meant for two applications to communicate with each other and often use JSON-formatted request & response data.

Django has a built-in method for converting Python data structures into JSON format and automatically setting the `Content-Type` header to `application/json`. For example:

```python
    def get_items(request):
        if name := request.GET.get("name"):
            student = Student.objects.get(name=name)
            response_data = {
                "name": student.name,
                "major": student.major,
                "year": student.year,
                "graduation": student.graduation,
            }
            return JsonResponse(response_data)
        
        # this code executes only if no 'name' parameter provided
        return JsonResponse({"errro": "student name not provided"})
```
This conversion from Python data to JSON-formatted text is called `serializing` and is necessary because the HTTP response must be plain text.

To serialize Python objects other than `dict` you must set the `safe` parameter to `False`:

```python
    return JsonResponse([1, 2, 3], safe=False)
```

### Django Rest Framework (DRF)

Explicitly parsing requests and serializing data for responses can get complicated, so Django applications often use [DRF](https://www.django-rest-framework.org/#quickstart). 

DRF abstract several key tasks for request & response handling:

- request parsing
- authentication & permissions checks
- response data serialization
- response pagination

DRF provides a complex set of capabilities, so this doc covers the most basic operations.

DRF supports both class-based and function-based views.

Because DRF is external to Django, it's necessary to add 'rest_framework' to your `requirements.txt` file and to the INSTALLED_APPS in your `settings.py` file:

```python
INSTALLED_APPS = [
    'rest_framework',
]
```

### DRF Serializers

Serializers are often defined as classes in a dedicated file called serializers.py for handy reference. This class specifies how a Django model or Python object should be serialized for HTTP responses.

```python
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    major = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    graduation = serializers.IntegerField()
```

- DRF has serializer methods that match Django DB data types
- the serializer returns a class instance a `data` attribute
- the serializer can be used to transform or validate request data before saving to a DB

This serializer class can be used anywhere in the application to serialize a single Student object or a list of Student objects. 

```python
serializer = StudentSerializer(student)
serializer.data
```

See [more details](https://www.django-rest-framework.org/api-guide/serializers/)

### DRF Views & ViewSets

DRF generic views allow you to quickly build API views that map closely to your database models.

For example, your views.py might have this basic view to show a list of Students from the DB:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from models import Student

class StudentsList(APIView):
    def get(self, request, format=None):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
```

Your `urls.py` needs to account for this class-based view.

```python
urlpatterns = [
    path('students/', views.StudentsList.as_view()),
]
```




