FROM python:3.9-slim-buster

#flask dependencies
COPY /app/requirements.txt /srv/sample-app/requirements.txt
RUN pip install --no-cache-dir -r /srv/sample-app/requirements.txt --src /usr/local/src

COPY /app/start.sh /app/gunicorn.conf.py /srv/sample-app/
WORKDIR /srv/sample-app/
RUN chmod +x ./start.sh

#flask app code
COPY /app/app.py /srv/sample-app

#startup script
CMD ["./start.sh"]