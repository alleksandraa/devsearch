# DevSearch

DevSearch is a website, which was the main part of a Django course, that is why it mostly focuses on the backend. The purpose of the website is to connect developers and find interesting projects. You can create your account, add projects and do all of the CRUD operations. You can also leave comments on other works and there is an intern inbox system.

## Technologies
- Python version: 3.10.5
- Django version: 4.0.3

## Initialize
Create .env file with enviromental variables in project's base folder with application secret key and database credentials:

```
SECRET_KEY = <project_secret_key>
DB_NAME = <database_name>
DB_USER = <database_user>
DB_PASSWORD = <database_password>
```

## Setup
Create and run an isolated environment:

```
$ python -m venv env
$ source env/bin/activate
```
Install the dependencies:


```
(env)$ pip install -r requirements.txt
```
Makemigrations and migrate:
```
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

To run the server:
```
(env)$ python manage.py runserver
```
