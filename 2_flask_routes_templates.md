## Flask Routes & Templating


### Reading

- https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing
- https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates
- https://flask.palletsprojects.com/en/2.2.x/quickstart/#accessing-request-data
- https://www.geeksforgeeks.org/retrieving-html-from-data-using-flask/

### Learning Outcomes

- Handling requests with parameters
- Handling POST requests
- Rendering complex output with templates

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Handle form submission"
    else:
        return "Show an HTML page"
```

You can also specify the single-method route like so:

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