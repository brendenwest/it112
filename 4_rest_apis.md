## Working with APIs

### Reading

- https://www.geeksforgeeks.org/how-to-return-a-json-response-form-a-flask-api/

### Learning Outcomes

- What are APIs?
- Flask API routes
- Serializing python objects
- Server-side API requests
- Server-side Caching

### What are APIs?

REST stands for Representational State Transfer and is an architectural style used in modern web development. REST apis use HTTP request/response constraints and typically return structured data for machine-to-machine communication. API response data can be in a variety of formats - e.g. XML, JSON, CSV, etc.

### Flask API Routes

Flask API routes are defined like any other routes, but usually return structured data instead of HTML.

Simple Flask api routes can use **jsonify** to return JSON data.

```python
from flask import Flask, jsonify
app = Flask(__name__)

# data is a Python dict
data = {"it112": 25, "it121": 18}

@app.get('/api/courses')
def courses():
    # send HTTP response with content-type: application/json
    return jsonify(data)

app.run(host='0.0.0.0', port=81)
```

API routes can receive and store data as well:

```python
@app.post('/courses')
def add_course():
    # normally we would validate the submission before adding to our list
    data.update(request.get_json())
    return '', 204
```

Returning Python objects and database query results as JSON data can be more complicated. 

Objects need to be **serialized** (converted to structured text), which usually requires you specify a **schema** for how each field in the object should be converted.

One simple approach - add a **serialize** property on the object class:

```python
# create a 'student' class that maps to a db table
class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  city = db.Column(db.String(50))

  @property
  def serialize(self):
    """Return object data in easily serializable format"""
    return {
      'id': self.id,
      'name': self.name,
      'city': self.city
    }
```

And then return the db query results as a list, based on that property:

```python
@app.route('/api/students')
def api_students():
  # return db query results as a JSON list
  return jsonify([student.serialize for student in Student.query.all()])
```

Python applicatoins typically use a serializer library such as [marshmallow](https://marshmallow.readthedocs.io/en/stable/) for more complex objects. 

### Server-side API Requests

Sometimes server applications need to retrieve data from another web service.

Flask applications can do this using the **requests** library.

```python
import requests
import json

@app.route('/api/data')
def api_data():
    url = "https://data.seattle.gov/resource/2khk-5ukd.json"
    try:
        result = requests.get(url)
        # since result is already JSON, it shouldn't be serialized again
        return app.response_class(
            response=result.text,
            status=200,
            mimetype='application/json'
        )
    except:
        return jsonify({"error": f"Unable to get {url}"})

```

For more on **scraping** sites with Flask, see - https://realpython.com/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/