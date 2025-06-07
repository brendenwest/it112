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

See more [DRF serializer details](https://www.django-rest-framework.org/api-guide/serializers/)

### DRF Views & ViewSets

DRF generic views allow you to quickly build API views that map closely to your database models.

For example, your views.py might have this basic view to show a list of Students from the DB:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from models import Student

class StudentDetail(APIView):
    """
    Retrieve or update  a record based on DB id (aka pk) extracted from query 
    """
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
        
    # update existing db record
    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # update existing db record
    def post(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentsList(APIView):
    """
    retrieve all Student from DB
    """
    def get(self, request, format=None):
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
```

Your `urls.py` needs to account for this class-based view.

```python
urlpatterns = [
    path('students/', views.StudentsList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),]
```

DRF also supports `function-based` views using the `@api_view` decorator:

```python
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from models import Student

    @api_view(['GET', 'POST'])
    def students(request):
        """
        Get all students or create a new record
        """
        if request.method == 'GET':
            students = Students.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET', 'PUT', 'DELETE'])
    def student_detail(request, pk):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = StudentSerializer(Student)
            return Response(serializer.data)
    
        elif request.method == 'POST':
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
```

### DRF Permissions

DRF includes a number of `permission` classes that can restrict who has access to a given view.

For example, adding this to the above views file will ensure that only authenticated requests get read-write access, and unauthenticated requests get read-only access.

```python
from rest_framework import permissions

# add this to each view class
permission_classes = [permissions.IsAuthenticatedOrReadOnly]
```

See more (DRF authentication details)[https://www.django-rest-framework.org/api-guide/authentication/].

