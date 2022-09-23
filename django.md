### Settings virtual enviroment:
install:
```
python –m pip install virtualenv
```
Create virtual enviroment

```
virtualenv env
```
Activate virtual enviroment

```
source env/bin/activate
```

### Install django
```
python -m pip install Django
```

### See version django
For verificatin of succesful instalation:
```
python -m django version
```
### Creating an application
1. execute command
```
django-admin startproject ecommerce-website
```
2. create startapp (inner directory created)
```
python manage.py startapp ecommerceSite
```
3. run server
* enter directory project and execute
```
python manage.py runserver
```
### Complete Initial Project Setup Django
```
python manage.py makemigrations
python manage.py migrate
```
### Create a superuser
```
(myprojectenv) $ python manage.py createsuperuser
```
### Install Gunicorn and Postgres adapter in Virtual environment
```
(myprojectenv) $ pip install django gunicorn psycopg2-binary
```
