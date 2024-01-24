FROM nginx:1.25.3-alpine

ARG NGINX_SERVER_HOSTNAME
ARG NGINX_SERVER_PORT

WORKDIR /home/app

COPY src/static ./static

COPY src/media ./media


RUN touch /etc/nginx/conf.d/custom.conf

RUN echo -e \
    "upstream django {\n" \
    "   server gunicorn:8000;\n" \
    "}\n"\
    "server {\n" \
    "   listen ${NGINX_SERVER_PORT};\n" \
    "   server_name ${NGINX_SERVER_HOSTNAME};\n" \
    "   location = /favicon.ico { access_log off; log_not_found off; }\n" \
    "   location /static/ {\n" \
    "     root /home/app/;\n" \
    "   }\n" \
    "   location /media/ {\n" \
    "     root /home/app/;\n" \
    "   }\n" \
    "   location / {\n" \
    "     proxy_pass http://django;\n" \
    "   }\n" \
    "}\n" > /etc/nginx/conf.d/custom.conf
