## Database Integration

### Reading

- https://www.w3schools.com/sql/default.asp
- https://www.tutorialspoint.com/flask/flask_sqlite.htm
- https://www.tutorialspoint.com/flask/flask_sqlalchemy.htm
- https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
- https://docs.sqlalchemy.org/en/14/tutorial/index.html (reference)

### Learning Outcomes

- Refresh on SQL & relational databases
- what is an ORM?
- Database operations with Python & SQLAlchemy
- Database operations with SQLAlchemy in a Flask application

### Overview

Server applications often need to store and retrieve persistent data. Relational databases are a primary choice for this but applications can also use `document` (aka schema-less or NoSQL) databases.

Python application developers can choose from a range of relational database systems (e.g. SQLite, PostgreSQL, MySQL, etc).

### Object Relational Mapper (ORM)

Python web applications can interface with a relational database using raw SQL (Structured Query Language), but often use an `ORM` that maps application classes (models) to relational database tables. ORMs can also simplify database queries and abstract syntax differences between database systems.

SQLAlchemy is a mature & popular ORM library for Python-based applications. 

First, you'll need to install SQLAlchemy in your application environment:

```commandline
pip install -U Flask-SQLAlchemy 
```

Then define one or more data models. A data model is a Python class with attributes that correspond to db table columns. Each attribute is defined with a data type (e.g. string, integer, date, etc.) and column settings such as:

- whether a column is the `primary key` for the table
- whether values should be unique
- whether the column can have `null` or blank values
- default value for the column

```python
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# set URI for the database to be used
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

# associate a SQLAlchemy object with the Flask app
db = SQLAlchemy(app)

# create a 'student' class that maps to a db table
class Student(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)  
   major = db.Column(db.String(50))

   def __repr__(self):
    return '<Student %r>' % self.name

# create / use the database
with app.app_context():
  db.create_all()
```

You can populate the database manually from an interactive Python shell like so (assuming your app is in `main.py`):

```python
~/$ flask --app main shell
>>> from main import db, Student
>>> db.create_all()
>>> student1 = Student(name='Neil deGrasse Tyson', email='neil@harvard.edu', major='astrophysics')
>>> student2 = Student(name='Nikole Hannah Jones', email='nikole@howard.edu', major='journalism')
>>> db.session.add(student1)
>>> db.session.add(student2)
>>> db.session.commit()
```

Then your Flask app can retrieve db records like so:

```python
  # retrieve all db records
  students = Student.query.all()

  # retrieve a single record
  student = Student.query.filter_by(id=2).first()
```