FROM nginx

COPY compose/nginx/nginx.conf /etc/nginx/nginx.conf
COPY compose/nginx/static_production /static
COPY compose/nginx/uwsgi_params /uwsgi_params
COPY compose/nginx/static_root_data /static_root_data
COPY compose/nginx/next /next

RUN mkdir -p /tmp/cache
RUN chmod -R 777 /tmp

EXPOSE 80

