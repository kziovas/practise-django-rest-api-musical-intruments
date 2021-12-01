## Practise Django REST API- Musical Instruments

The project is meant to be a starting point, an experimentation or a basic example of a way to develop an API with Django. 
It is an exercise on using Django and various python technologies and design methodologies.

Methodologies used:
  - MVC(Model-View-Controller) pattern
  - Data transfer Objects (DTOs)
  - Object relational mapper (ORM)
  - API building conventions from  [OpenAPI specfifications](https://swagger.io/specification/)
  - Dependency injection
  - Class based views and ViewSets routing
  - Containerization


Tools used:
  - Django
  - MySQL
  - Django REST framework
  - Docker
  - Docker Compose (for orchestration)
  - Injector

---

## Installation and deployment

The API can be run in two ways:

  - As a Docker container
  - As a standalone API service on the localhost


#### Run service with Docker

To run it in a Docker container simple `git-clone` the repo and `cd` to the directory where the `docker-compose.yml` file is located.

Execute `docker-compose up` in this directory. Two containers should start, one that hosts the MySQL server for our database and one which hosts the actual django application.

The application will try to connect to the database. If the database that is trying to connect does not exist, it has to be first created in MySQL.
This can be done either by the terminal inside the container or through the MySQL workbench. Some information can be found here: [Create a database in a Docker container for local development](https://developer.ibm.com/tutorials/docker-dev-db/). The default database details set in this project can be seen in the snippet below.

If the database was already created, the service will connect to it automatically.

#### Run service in localhost

For easier testing and debugging the application can be run in the localhost by moving to the directory where the `manage.py` file is and execute the command:
`python manage.py runserver 0.0.0.0:8080`

A MySQL server must exist in the localhost and a database should also exist in MySQL that matches the database details found in the `core/settings.py`. The default details that were set in the project can be seen below.

<pre>
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "instruments_db",
        "USER": "instruments_admin",
        "PASSWORD": "instruments",
        "HOST": "db",
        "PORT": "3306",
    }
}
</pre>
 

