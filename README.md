## Local run

#### Create .env file from .env-example and set all data

```sh
$ docker-compose build --no-cache
$ docker-compose up
$ docker-compose run backend python backend/manage.py makemigrations
$ docker-compose run backend python backend/manage.py migrate
$ docker-compose run backend python backend/manage.py createsuperuser
$ docker-compose exec postgres bash
```

### Local urls

```
$ http://0.0.0.0:8000/admin/
$ http://0.0.0.0:8000/employees/ - list and create employees
$ http://0.0.0.0:8000/employee-detail/<int:pk>/ - Detail Update Destroy
$ http://0.0.0.0:8000/store-list/ - list store, see only related employees
$ http://0.0.0.0:8000/store-detail/<int:pk>/ - Visit store
$ http://0.0.0.0:8000/store-create/ - create store

```