# address_book
## About
Python django application for creating/view/edit contacts with corresponding search by all the fields.
Supports CI and CD AWS EC2 workflows
Application is run via docker containers

## Prerequisites
* Install docker https://docs.docker.com/engine/install/
* Install docker compose https://docs.docker.com/compose/install/

## Configure envs

### Important! Change DJANGO_SECRET_KEY before usage!

Django config: src/.env
```
DJANGO_DEBUG_MODE=false
DJANGO_SECRET_KEY=django-insecure-i00tygfvwjav1f%5qsu9)otzd&7k*hj^57=qdvoxg^5d=ac8lw
```

Nginx config: .env
```
NGINX_SERVER_HOSTNAME=localhost
NGINX_SERVER_PORT=80
```

## Run database migration
```
docker compose run gunicorn python3 manage.py makemigrations
docker compose run gunicorn python3 manage.py migrate
```

## Run server with following command

```
docker compose up
```
