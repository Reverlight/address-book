# address_book
## How to install
Application for creating contacts with corresponding search by all the fields.
* Install python 3
* Create virtualenv
* Git clone https://github.com/Reverlight/address_book.git
* Use following commands for set-up using virtualenv:

## Configure envs

### Important! Change DJANGO_SECRET_KEY before usage!

Django config: src/.env
```
DJANGO_DEBUG_MODE=false
DJANGO_SECRET_KEY=django-insecure-i00tygfvwjav1f%5qsu9)otzd&7k*hj^57=qdvoxg^5d=ac8lw
```
### When you deploy to production do not forget to change localhost to host machine IP address
Nginx config: .env
```
NGINX_SERVER_HOSTNAME=localhost
NGINX_SERVER_PORT=80
```

```docker-compose up gunicorn manage.py migrate```

## Run server with following command

```docker-compose up```
