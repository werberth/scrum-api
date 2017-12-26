# Scrum Board API

Scrum Board API project exemple from the book [Lightweight Django by Julia Elman and Mark Lavin (O’Reilly). Copyright 2014.](http://www.amazon.com/Lightweight-Django-Julia-Elman/dp/149194594X/)

## Terms and Conditions

Please assume the terms and conditions transfer from the examples from the book at [github.com/lightweightdjango](https://github.com/lightweightdjango/examples).

## Installation

```
git clone git@github.com:werberth/scrum-api.git scrum-api
cd scrum-api
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

 - Rename the exemple.env file to .env and set the ```DEBUB``` variable to ```True```.
 - If you want to use PostgreSQL, replace the username for the database username, the password for the user's password, and database_name for the database name. Example:

 	```DATABASE_URL='postgres://username:password@localhost/database_name'```

 	Taking as an example a database with name "scrum_database", and a user with username "admin" and password "12345":

 	```DATABASE_URL='postgres://admin:12345@localhost/scrum_database```
 - Run ```python manage.py runserver``` 

 ## Using the API

 ### URLs

 - **API Root**
 	- ```localhost:8000/api/token/ [name='api-token']```
	- ```localhost:8000/api/[name='api-root']```
	- ```localhost:8000/api/(?P<format>[a-z0-9]+)$ [name='api-root']```
- **Sprint App**
	- ```localhost:8000/api/sprints/$ [name='sprint-list']```
	- ```localhost:8000/api/sprints/\.(?P<format>[a-z0-9]+)$ [name='sprint-list']```
	- ```localhost:8000/api/sprints/(?P<pk>[^/.]+)/$ [name='sprint-detail']```
	- ```localhost:8000/api/sprints/(?P<pk>[^/.]+)/\.(?P<format>[a-z0-9]+)$ [name='sprint-detail']```
- **Tasks App**
	- ```localhost:8000/api/tasks/$ [name='task-list']```
	- ```localhost:8000/api/tasks/\.(?P<format>[a-z0-9]+)$ [name='task-list']```
	- ```localhost:8000/api/tasks/(?P<pk>[^/.]+)/$ [name='task-detail']```
	- ```localhost:8000/api/tasks/(?P<pk>[^/.]+)/\.(?P<format>[a-z0-9]+)$ [name='task-detail']```
- **Users Routes (Read Only)**
	- ```localhost:8000/api/users/$ [name='user-list']```
	- ```localhost:8000/api/users/\.(?P<format>[a-z0-9]+)$ [name='user-list']```
	- ```localhost:8000/api/users/(?P<username>[^/.]+)/$ [name='user-detail']```
	- ```localhost:8000/api/users/(?P<username>[^/.]+)/\.(?P<format>[a-z0-9]+)$ [name='user-detail']``` 