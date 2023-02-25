## Django Queries

### Reading

- Web Development with Django, CH. 2 (read operations)
- https://www.w3schools.com/django/django_queryset.php
- https://docs.djangoproject.com/en/4.1/topics/db/queries/
- https://docs.djangoproject.com/en/4.1/ref/models/querysets/
- https://books.agiliq.com/projects/django-orm-cookbook/en/latest/introduction.html 

### Learning Outcomes

- Queries to create, read, update, & delete DB records
- Queries with conditions
- Chaining queries
- Using Django QuerySets in python

### Creating a Record

```python
    from students.models import Student
    # create a python object based on Student class
    student = Student(name="Malcolm X", graduation=2023, year="SR")
    # save data to DB
    student.save()
```

### Read Operations

Django DB operations mostly use the `objects` attribute of each data model. 

The `all()` method returns all records in the corresponding DB table:
```python
    # get all records
    # similar to "select * from appname_students"
    students = Student.objects.all()    
```

The `get()` method returns exactly one record in the corresponding DB table, based on a field criteria. 

Django throws an error if there is no match, or if the query would return more than on record, so it's common to wrap this in a `try ... except` block:

```python
    from django.core.exceptions import ObjectDoesNotExist
    try:
        # get a single record
        malcolm = Student.objects.get(name="Malcolm X")
    except ObjectDoesNotExist:
        print("Malcolm not found")
    except Exception as e:
        # some other error
        print(e)
```

Django apps can query for DB records that match certain conditions using the `filter()` method.

```python
    # return all students who are seniors
    seniors = Student.objects.filter(year='SR')
```

Filter conditions can be combined to behave like a SQL `AND` clause:

```python
    # return all students who are seniors and graduating in 2023
    seniors = Student.objects.filter(year='SR', graduation=2023)
```
A SQL `OR` clause is a bit more complicated. You can either combine two queries:
```python
    seniors = Student.objects.filter(
            year='SR'
        ) | Student.objects.filter(
        graduation=2023
    )
```
Or you can use Django's `Q` object which supports advanced query logic:

```python
    from django.db.models import Q
    seniors = Student.objects.filter(Q(year='R')|Q(graduation=2023))
```

### Django Querysets

Most Django read operations return a `QuerySet` collection that can be iterated.

```python
    students = Student.objects.all()
    print(students)
    <QuerySet [<Student: Malcom>, <Student: David>]>
```

Querysets are `lazy`, meaning a QuerySet can be constructed, filtered, sliced, and generally passed around in Python without actually hitting the database until you do something to evaluate the queryset.

You can inspect the SQL command that Django would execute:

```python
    str(students.query)
```

A QuerySet is iterable (like a list) and executes its DB query the first time you iterate over it.

```python
    for student in Student.objects.all():
        print(student.name, student.year)
```

QuerySets support python slicing and also have helper methods:

```python
    students = Student.objects.all()
    print(students.count())
    print(students.first())
    print(students.last())
    print(students[:2])
```

QuerySets can be converted to a python list. This forces evaluation of the DB query:

```python
    students_list = list(Student.objects.all())
```

QuerySets support a wide range of supporting methods that can be chained. For example, to `sort` results:

```python
    # order student results by graduation year (descending) and name
    Student.objects.all().order_by('-graduation', 'name')
```