# qBay - Python-CI-2021 template

[![Pytest-All](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/pytest.yml/badge.svg)](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/pytest.yml)
[![Python PEP8](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/style_check.yml/badge.svg)](https://github.com/CISC-CMPE-327/Python-CI-2021/actions/workflows/style_check.yml)

### Frontend

In order to understand every single bit of this template, first please try cloning the repository, running it, registering a user, logging in, and logging out to develop a general sense of what is going on: 

```
python -m qbay 
```

Next, try to read the python code from the entry point, starting from `qbay/__main__.py` file. It imports a pre-configured flask application instance from `qbay/__init__.py`. In the init file, `SECRET_KEY` is used to encrypt the session data stored in the client's browser, so one cannot just tell by intercepting your traffice. Usually this shouldn't be hardcoded and read from environment variable during deployment. For the seak of convinience, we hard-code the secret key here as a demo.

When the user type the link `localhost:8081` in the browser, the browser will send a request to the server. The client can type different routes such as `localhost:8081\login` or `localhost:8081\register` with different request methods such as `GET` or `POST`. These different routes will be handled by different python code fragments. And those code fragments are all defined in the `qbay/controllers.py` file. For example:

```python
@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')
```

The first line here defines that if a client request `localhost:8081\register` with the 'GET' method, this fragment of code should handle that request and return the corresponding HTML code to be rendered at the client side. For example, if the user type `localhost:8081\register` on his/her browswer and hit enter, then the browser will send a GET request. The above fragment of code recieve the request, and the last line looks up for a HTMP template named `register.html` in the `qa327.templates` folder.
```html
{% extends 'base.html' %}

{% block header %}
<h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
<h4>{{message}}</h4>
<form method="post">
  <div class="form-group">
    <label for="email">Email</label>
    <input class="form-control" name="email" id="email" required>
    <label for="name">Name</label>
    <input class="form-control" name="name" id="name" required>
    <label for="password">Password</label>
    <input class="form-control" type="password" name="password" id="password" required>
    <label for="password">Confirm Password</label>
    <input class="form-control" type="password" name="password2" id="password2" required>
    <input class="btn btn-primary" type="submit" value="Register">
  <a href='/login' class="btn btn-primary" id="btn-submit" >Login</a>
  </div>
</form>
{% endblock %}
```

Let's break this down. This is the Jinja Templating format (full synatx documentation here)：

https://jinja.palletsprojects.com/en/2.11.x/templates/

In contrast to React, Vue or other frameworks, it is a server-side rendering framework. It means that the job of filling the template with the required information is done on the server, and the final html will be sent to the client's browswer. Client side rendering is also becoming very popular, but it is very important to understand how different things work. 

The firstline calls a base template, if you open it, you will find a large chunk of html code. That is the base template for all webpages so we can share common HTML/CSS/JS code for all templates. In line ~127 of the base.html template, you can find something like:

```html
    <div class="col-lg-8">
        {% block content %}{% endblock %}
    </div>
```

It defines a block named `content`. This block can be replaced by any block definitions in other templates that use the base template. So in this example, `register.html` defines a block also named `content`, this block will replace the `content` block in the base template. So everything in the content block of `register.html` will be inserted into `base.html`. 

On `register.html` there is also a line: 

```html
<h4>{{message}}</h4>
```
This will be replaced by the same named parameter, in this case `message`, in the params of `render_template` function call. If we go back `controllers.py` python code earlier, we see:

```python
@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')
```

Here the message param is an empty string. So when rendering the template, `{{message}}` will be replaced by an empty string. 
Then completed the whole registration page will be returned to the browser. That will be the page you saw on the register URL.

Once the client got to the register page, he/she can submit the form with input information. The form by default, after the user clicked the submit button, will be `POST`ed to the same URL, so in this case, 'localhost:8081/register'. Now the server recieves the browswer's request, and need to find the corresponding code fragment to handle the request of route `/register` and method `POST`. It looks up the defined routes, and we have the following match in `controllers.py`:

```python
@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    if password != password2:
        error_message = "The passwords do not match"
    else:
        # use backend api to register the user
        success = register(name, email, password)
        if not success:
            error_message = "Registration failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')
```

So this fragment of code will read the data from the form, as you can tell from the first 4 lines of function `register_post`. Then, it calls a backend function to register the user. If there is any error, the backend will return an error message, describing what is the problem. If there is any error message, we will return the original `register.html` template to the client with the error message replaced the `{{message}}` snippet in the template.

