## Flask Routes & Templating


### Reading

- https://www.w3schools.com/tags/ref_httpmethods.asp
- https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing
- https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates
- https://flask.palletsprojects.com/en/2.2.x/quickstart/#accessing-request-data
- https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/
- https://jinja.palletsprojects.com/en/3.1.x/templates/

### Learning Outcomes

- Basics of Flask routes
- Handling HTTP requests with parameters
- Handling POST requests
- Rendering HTML output with templates

### Routes

The `route()` decorator binds a `function` to a url, where the parameter in parentheses corresponds to the url pattern.

```python
@app.route('/')
def index():
    # this is the site default url
    return 'Home Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
```

You can specify `patterns` for dynamic urls, enclosing a variable name within brackets. The corresponding url parameter is passed to the function as a variable.

```python
@app.route('/user/<username>')
def show_user_profile(username):
    # show info for requested username
    return f'User {escape(username)}'
```

For more details, see https://flask.palletsprojects.com/en/2.2.x/quickstart/#variable-rules


### HTTP Methods

By default, Flask routes handle GET requests, but you can specify exactly which HTTP methods a route should handle.

```python
from flask import request

# this route handles GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Handle form submission"
    else:
        return "Show an HTML page"
```

You can also specify a single-method route like so:

```python
@app.get('/login')
def login_get():
    # handle GET request
    return show_the_login_form()

@app.post('/login')
def login_post():
    # handle form submission
    return do_the_login()
```

For more details, see https://www.tutorialspoint.com/flask/flask_http_methods.htm

### Handling Request Data

Flask routes can operate on data sent to the server as query parameters or form fields using the `request` module.

- Query parameters are accessed from the `request.args` collection
- Form fields are accessed from the `request.form` collection

```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/user')
def user():
    # get the query parameter from /user?name=some-name
    return f"Hello {request.args.get('name')}"

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      # get the name field from form submission
      return f" {request.form.get('name')}"

```

For more details see https://www.tutorialspoint.com/flask/flask_request_object.htm

### Templates

Generally, it's not desirable to mix large amounts of HTML content with Python code, so Flask supports `templates` that mix dynamic data with static HTML at run time. Flask uses `Jinja2` templates by default.

A Jinja template is simply a text file with any extension.

Jinja template syntax is not a full programming language, but supports `variables` and/or `expressions`, which Flask replaces with values when the template is rendered. A template can also contain `tags` for basic logic control. 

Jinja uses several kinds of delimiters to indicate where data should be replaced:

- {% ... %} for programmatic Statements
- {{ ... }} for Expressions to evaluate & output 
- {# ... #} for Comments not included in the template output

For example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    {# this is a comment #}

    {% if student_name %}
        <h1>Course Schedule for {{ student_name }}</h1>
    {% else %}
        <h1>Course Schedule Page</h1>
    {% endif %}
    
    <ul>
    {% for course in courses %}
        <li><a href="/courses/{{ course.id }}">{{ course.name }}</a></li>
    {% endfor %}
    </ul>

</body>
</html>
```

Flask routes can use a template to `render` HTML output. 

Templates must be in the `/templates` directory of the Flask project.

Flask can pass python data variables to `render_template` as parameters for use in output generation.

```python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/schedule/<student_name>')
def schedule(student_name):
courses = [
  {"id": 123, "name": "IT 121"},
  {"id": 456, "name": "IT 276"},
  {"id": 789, "name": "MATH 140"},
]
return render_template('schedule.html', student_name=student_name, courses=courses)
```


