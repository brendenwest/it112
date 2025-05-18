## Django Models

### Reading

- Web Development with Django, CH. 2
- https://www.w3schools.com/django/django_models.php
- https://www.w3schools.com/django/django_queryset.php
- https://docs.djangoproject.com/en/5.2/topics/db/queries/
- https://docs.djangoproject.com/en/5.2/ref/models/querysets/
- https://books.agiliq.com/projects/django-orm-cookbook/en/latest/introduction.html

### Learning Outcomes

- Database definition in Django
- Django Object Relational Mapping (ORM)
- Database change management
- Basic DB read/write operations
- Queries with conditions & chaining
- Using Django QuerySets in python


### Overview

As noted earlier, Django is a database-centric web framework with significant built-in features for relational DB integration.

Django supports a variety of supported relational DB's (e.g. SQLite, MySQL, PostgreSQL, Oracle, etc), and the Django ORM (Object-Relational Mapping) hides the differences between these systems.

This section assumes familiarity with relational DB concepts and SQL query language, although they are covered in the readings.

### The Django ORM

The Django ORM converts object-oriented Python code into actual database constructs such as database tables or SQL queries, allowing a full range of database operations via simple Python code.

An application's database backend is specified in the *settings.py* file.

### Django Models

Django allows definition of DB tables through python classes (**models**) with fields that correspond to DB columns. Models are stored in a `models.py` file.


```python
from django.db import models

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    graduation = models.IntegerField(blank=True)
    year = models.CharField(max_length=25, choices=YEAR_IN_SCHOOL_CHOICES, )
```

- `Student` corresponds to the `appname_student` DB table
- Each data type corresponds to a supported DB data type
- Field definition can included constraints such as uniqueness, length, default & allowed values, and whether empty values are allowed
- By default Django creates a unique, auto-incrementing `id` field unless you specify a `primary key` field

See full details of Django model fields at https://docs.djangoproject.com/en/4.1/ref/models/fields/

### Django Migrations

Django manages database structure updates through `migrations` so you can easily track & revert changes if needed.

As models are defined or updated, you will need to generate a `migration` like so:

```python
    python manage.py makemigrations <appname>
```

This will create an auto-numbered file like so - `appname/migrations/0001_initial.py` with python code to update the database.

You can see what SQL statements a migration will perform with this command:

```python
    python manage.py sqlmigrate appname 0001_initial
```

You can apply any mode changes (migrations) like so:

```python
    python manage.py migrate appname
```

### Model Methods

Django models can also contain methods to simplify interaction with objects defined in the class. Model methods can be custom or can override methods inherited from the base model class.

For example, the above `Student` model might use `__str__` to provide a custom description of model instances:

```python
    def __str__(self):
        return f"{self.name}, {self.year}"
```
 
### Basic DB Operations

You can perform operations on a DB using your python model. The operations can be in a python script or executed via Django's interactive shell:

```python
    python manage.py shell
```

Before performing any operations, you need to import the model:

```python
    from appname.models import Student
```

#### Creating a DB entry

```python
    import datetime # we'll need this to create data values

    dob = datetime.date(2001, 08, 19)
    student = Student(name="Darren Black", date_of_birth=dob, graduation=2024, year="FR")
    student.save()  # create the entry in DB

    dob2 = datetime.date(2002, 09, 19)
    # define & save student in one step
    student2 = Student.objects.create(name="Alice White", date_of_birth=dob, graduation=2025, year="SO")
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