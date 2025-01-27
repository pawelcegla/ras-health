FROM python:3.13-alpine
WORKDIR /opt
RUN pip install Flask Flask-HTTPAuth pyuwsgi
COPY app.py /opt
EXPOSE 8000
CMD [ "uwsgi", "--http", "0.0.0.0:8000", "-p", "1", "--wsgi-file", "app.py", "--callable", "app" ]
