FROM python:3.9-buster

mkdir -p /var/app/djangoapp/
COPY src/ /var/app/djangoapp/

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]