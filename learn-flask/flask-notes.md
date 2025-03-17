# Learn Flask

The "hello world" of flask. Put the following code in a file named `hello.py`.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

And to run this in development mode -

```shell
flask --app hello run
```

A lot of magic went behind the scenes to make this happen. 

## Flask CLI

First lets understand how `flask` executable works. Even though in production I'd never use this executable, it is nonetheless useful to understand this so I can follow along other examples, tutorials, etc. none of which will explain how this works. Main reference documentation [Command Line Interface — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/cli/).

### Specifying the App

The main command that is used to run an app is `run`, so I'd call `flask run` with some more arguments, flags, etc. The basic information that we need to give Flask is the name of the python module which has the Flask app, and the name of the variable that points to the instantiated Flask application. Flask uses the **optional** `--app` argument for this. This is optional because of some default behavior that we'll cover after we understand the explicit behavior of this argument. This argument has three parts - 

1. The current working directory
2. The "main" python module
3. The variable name of the instantiated Flask app 

![fig-1](./fig-1.png)

I can run the above command to run the app inside the `example-2` directory. I am telling Flask that inside the `example-2` directory it will find a python package called `web` and inside that package it will find the main python module called `hello` which has a varaible named `app` which references the `Flask` application object.

Instead of the instance variable, I can also specify a function that returns the instance.  These so-called "factory" functions are useful when using [Blueprints](https://flask.palletsprojects.com/en/2.3.x/blueprints/). See `example-4` for a demo. The app is run as -

```shell
flask --app example-4/web.api:create_app run
```

Here `web/api/__init__.py` has the `create_app` function so that becomes my main python module. I can now browse to http://127.0.0.1:5000/one or http://127.0.0.1:5000/two to see the two different "apps" in action.

If neither the instance variable nor the factory function is provided Flask will first look for instance variables named `app` or `application` and use these as default. If it does not find this it will look for factory functions named `create_app` or `make_app`. So I could've run `example-2` as `flask --app example-2/web.api.hello run` and `example-4` as `flask --app example-4/web.api run`.



The main python module can be specified as a stand-alone python file with its full path, or using the usual dotted python package notation.

If the stand-alone python module is in the current directory, i.e., in `./hello.py` then just running `flask --app hello run` is enough. Flask will look in the pwd for a python file named hello and "run" it (more on how it is run later).

Lets say I have the following directory structure (as demonstrated in `example-1` directory) -

```
web
└── api
    └── hello.py
```

Then I can run the app with -

```shell
cd example-1
flask --app web/api/hello run
```

And if `web` is a package, i.e., I have the following directory structure (as demonstrated in `example-2` directory) -

```
web
├── __init__.py
└── api
    ├── __init__.py
    └── hello.py
```

then I can run the app with -

```shell
cd example-2
flask --app web.api.hello run
```

Of course I could've had the contents of `hello.py` inside `__init__.py` like so (see `example-3`) -

```
web
├── __init__.py
└── api
    └── __init__.py --> contains the same code as hello.py
```

Now I can run this with -

```shell
cd example-3
flask --app web.api run
```

In all the above examples I change the directory into the appropriate examples directory so that Flask can find the package/module. However, I don't have to do this, I can also specify the current working directory as part of the argument. E.g., if I want to run `example-3` directly from `learn-flask` directory I can do -

```shell
flask --app example-3/web.api run
```

Here I am explicitly specifying the current working directory for Flask as it is different from my present working directory. Of course if it is not explicitly specified, the pwd is assumed to be cwd.



As mentioned earlier `--app` is an optional argument. If I don't provided it, Flask will look for a python module file by the name of `app.py` or `wsgi.py`. It does not seem to work with packages. See `example-5` for a non-demo. But in the root directory if I just `flask run`, then it will pick up the `./app.py` and use that as the main module.

### Environment Variables

Instead of calling `flask run` with a bunch of arguments, I can specify the same arugments in environment varialbes in the form of `FLASK_{OPTION}` or `FLASK_{COMMAND}_{OPTION}`, e.g., `FLASK_APP` or `FLASK_RUN_PORT`, etc.

If there is a `.env` file in the directory `flask` is run from, **and**, the `dotenv` package is installed, Flask will set the environment variables in there. Additionally Flask will also load a `.flaskenv` file if it exists. The basic idea is that `.flaskenv` file is supposed to have public settings that can be checked into a repo, whereas `.env` is supposed to have private settings that should not be checked in. See `example-6` for a demo.

### Debugging

Just pass the `--debug` flag when calling `flask run --debug`. This will enable the "interactive debugger" where the stacktrace will be returned as a response. Not much use in API servers and no idea where the interactivity comes from. Note, the stacktrace is already printed out to the console. The more useful feature of setting the debug flag is that the app will be auto reloaded if any of the files are changed.

### Custom Commands

In addition to built-in commands like `run` I can create my own commands for `flask`. Seems like a bad anti-pattern unless there is some reason I need the application context for that custom command. In most cases I am better off creating a one-off script to do the job. I have to decorate the relevant function with `app.cli.command()` and then I am able to call that command from `flask` CLI. Example -

```python
import click
from flask import Flask

app = Flask(__name__)

@app.cli.command("create-user")
@click.argument("name")
def create_user(name):
    ...
```

```shell
flask create-user admin
```

The above command will invoke the `create_user` function and pass `admin` as the `name` argument to it. There are a bunch of other ways to do this, e.g., using `app.cli.add_command()` and so on. Won't spend time learning/documenting this.

## Deploying

In production it is not recommended to use the `flask` executable. There are a bunch of alternatives [available](https://flask.palletsprojects.com/en/3.0.x/deploying/). The two common-sense ones are -

* Nginx as the reverse proxy with Gnunicorn running behind it.
* mod_wsgi running as part of Apache httpd server.

When using mod_wsgi, I'll need a small script that loads the Flask app, but it has to be called `application` not anything else 🤷🏾‍♂️. Here is sample script called `wsgi.py` along with its invocation -

```python
from hello import app

application = app
```

Or, I can create the app using the factory function like so -

```python
from hello import create_app

application = create_app()
```

And then start the server as -

```shell
mod_wsgi-express start-server wsgi.py --processes 4
```

`--processes` flag specifies the number of worker processes, a good deafult is twice the number of available CPU cores.

## Logging

The most straightforward thing I can do is use `app.logger` to get the global Python `logging.Logger` object and use it like I do in any other Python program. If I want to configure the logger I need to do it before I instantiate the `Flask()` application object. See `example-7` for an example. The log format that I specify there is the default format of Apache httpd. [Logging — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/logging/) has a more complete log config using `dictConfig` instead of `basicConfig`.

## Configuration

There are a lot of patterns mentioned in [Configuration Handling — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/config/) to get a cascading config setup. But the simplest is to use `app.config.from_envvar(ENV_VAR_NAME)` function. This looks for an environment variable called `ENV_VAR_NAME` and tries to load the python file that is pointed to by that environment variable. The python file contains the config. I can give any extension to this file (e.g., .cfg) but it will be parsed as a Python file by Flask. **Only all caps variables will available as config**. So I can have something like the following in `dev.cfg` -

```python
TESTING = True
ENV = "dev"
DATABASE_URI = "sqlite:////tmp/foo.db"
```

Load the config as follows in my app.py -

```python
app = Flask(__name__)
app.config.from_envvar("EXAMPLE8_CONFIG")

# Now access the config values as app.config["ENV"]
```

And then before starting the app I set the `EXAMPLE8_CONFIG` environment variable to the full path of `dev.cfg` -

```shell
export EXAMPLE8_CONFIG=/full/absolute/path/to/dev.cfg
flask run
```

Providing the full absolute path can be inconvenient or downright impossible in production environments. In this case Flask assumes that there is a special directory called `instance` at the same level as the top level package or the actual main python file. Then I can specify the config file relative to this directory. The only difference is that I need to tell Flask to use instance directory for loading configs. See `example-8` for a full example. I can run that example as -

```shell
export EXAMPLE8_CONFIG='dev.cfg'
flask --app flask_app run
```

## REST APIs

Any function in the main Python module can be the API. All I need to do is decorate it with `@app.get("/path")` for it to serve a GET request. I can use the appropriate method on `app` that matches the HTTP verb I want to serve like `@app.put()` or `@app.post()` and so on. If my function returns a list or a dict, it is automatically converted to a JSON response, i.e., the right `Content-Type` is set to `application/json` is set and so on. There is a function called `jsonify` that can do the same thing and returns a `Response` object. Flask is internally calling `jsonify` with the list or dict that my function returns. No need for me to do that. See `example-9` for a demo.

## Testing

The Flask application instance has a method called `test_client` which can be used to make GET, POST, etc. requests using the appropriatly method names, very similar to `requests`. This will return a `TestResponse` object which is a subclass of the main `Response` object. I can call methods like `get_json()` to get the payload and then use the usual `assert` statements. For a more detailed explanation see [Testing Flask Applications — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/testing/). See `example-9` for a simple example. A more involved demo is included as part of the [flask example tutorial](https://github.com/pallets/flask/tree/main/examples/tutorial/tests). 

## Application and Request Lifecycle

[Application Structure and Lifecycle — Flask Documentation (3.0.x)](https://flask.palletsprojects.com/en/3.0.x/lifecycle/#how-a-request-is-handled)

Basic idea is that for every request Flask will create the application context which makes `g` and `current_app` objects available. Then it will create a request context which will make the `request` and `session` objects available.

### Application Context

The `app` Flask application object has a bunch of useful methods/properties like `app.config` and `g`. `g` is a "global" object within the current application context. It is a simple namespace object that can be used to hold any objects that are needed from the start of the request to the end of it. A typical use is to store the db connection handle here. The usual pattern is to have a function called `get_X` to add `g.X` to the namespace and `teardown_X` to "clean up" if any is needed. Here is how database connection can be stored here -

```python
from flask import g

def get_db():
    if 'db' not in g:
        g.db = connect_to_database()

    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
@app.get("/me")
def me():
  db = get_db()
  user = db.select_current_user()
  ...
```





