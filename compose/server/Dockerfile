FROM hagen013/alpine:latest

# INSTALL REQUIREMENTS
COPY  services/server/requirements/base.txt base.txt
COPY  server/requirements/production.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# COPY ENTRYPOINT AND CODE
COPY  services/server /server
COPY  services/client /client
COPY  compose/server/uwsgi.ini uwsgi.ini
COPY  compose/server/entrypoint.sh entrypoint.sh

RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8001

ENTRYPOINT ["/entrypoint.sh"]
