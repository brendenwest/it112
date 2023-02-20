## Django Models

### Reading

- Web Development with Django, CH. 2
- https://www.w3schools.com/django/django_models.php

### Learning Outcomes

- Database definition in Django
- Django Object Relational Mapping
- Database change management


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

- `Student` corresponds to the `<appname_student` DB table
- Each data type corresponds to a supported DB data type
- Field definition can included constraints such as uniqueness, length, default & allowed values, and whether empty values are allowed
- By dfault Django creates a unique, auto-incrementing `id` field unless you specify a `primary key` field

See full details of Django model fields at https://docs.djangoproject.com/en/4.1/ref/models/fields/

### Django Migrations

Django manages database structure updates through `migrations` so you can easily track & revert changes if needed.

Once models are defined or updated, you will need to generate a `migration` like so:

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
    student = new Student(name="Darren Black", date_of_birth=dob, graduation=2024, year="FR")
    student.save()  # create the entry in DB

    dob2 = datetime.date(2002, 09, 19)
    # define & save student in one step
    student2 = Student.objects.create(name="Alice White", date_of_birth=dob, graduation=2025, year="SO")
```

#### DB Read Operations

Django interacts with tables through the `objects` attribute of a model. Read operations typically use `get()` for single records, `all()` for all records, or `filter` for records that meet a criteria.

```python
    # get all records. returns a collection
    students = Student.objects.all()
    
    # get records that meet a condition
    sophomores = Student.objects.filter(year="SO")

    # get a single record
    student = Student.objects.get("name=Darren Black")
```
