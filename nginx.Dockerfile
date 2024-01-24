FROM nginx:1.25.3-alpine

WORKDIR /home/app

COPY src/static ./static

COPY src/media ./media


RUN touch /etc/nginx/conf.d/custom.conf

RUN echo -e "upstream django {" \
            "server gunicorn:8000;" \
          "}"\
          "server {" \
            "listen 80;" \
            "server_name localhost;" \
            "location = /favicon.ico { access_log off; log_not_found off; }" \
            "location /static/ {" \
              "root /home/app/;" \
            "}" \
            "location /media/ {" \
              "root /home/app/;" \
            "}" \
            "location / {" \
              "proxy_pass http://django;" \
            "}" \
          "}" > /etc/nginx/conf.d/custom.conf
