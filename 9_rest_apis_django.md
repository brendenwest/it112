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
