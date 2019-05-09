FROM alpine:latest

# BASE PACKAGES
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    build-base \
    libffi-dev \
    linux-headers \
    && pip3 install --upgrade pip \
    && pip3 install --no-cache-dir psycopg2

# UWSGI
RUN apk add --no-cache uwsgi uwsgi-python3 uwsgi-python uwsgi-http uwsgi-corerouter uwsgi-stats_pusher_socket

# PILLOW 
RUN apk add --no-cache \
    py3-pillow

# BASH
RUN apk add --update --no-cache bash
