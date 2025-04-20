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

Server applications often need to store and retrieve persistent data. Relational databases are a primary choice for this purpose.

Python Developers can choose from a range of database systems (e.g. SQLite, PostgreSQL, MySQL, etc) and Object Relational Mapper (ORM) libraries.

An `ORM` (Object Relational Mapper) maps program classes (or models) to relational database tables. It allows a program to implement database CRUD operations without raw SQL statements.

SQLAlchemy is a mature & popular ORM choice for python-based applications.

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