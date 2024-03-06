# MATEXAPPLICATION
Software Engineering Assignment

**Getting started**

**Requirements:**
- [python](https://www.python.org)

**Mac**
- setup a virtual environment: `python3 -m venv env`
- start the virtual environment: `source .venv/scripts/activate`
- install django: `pip3 install django`
- run the web app: `python3 manage.py runserver`

**Windows**
- create the virtual environment: `py -3 -m venv .venv`
- start the virtual environment: `.venv\scripts\activate`
- install dependencies: `pip install -r requirements.txt`

**Resources**
- [VSCode Guide to Django](https://code.visualstudio.com/docs/python/tutorial-django)

**Dependency management**
- perform the following steps while the virtual environment is active.
- whenever a new dependency is added generate a new dependency list using
`pip freeze > requirements.txt` and push changes.
- When a dependency has been added by another user, pull main and install
dependencies using `pip install -r requirements.txt`
- By doing this everyone's virtual environment will remain up to date.
