#!/bin/sh

cd /app

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Applying database migrations"
python manage.py makemigrations --noinput

echo "Applying database migrations"
python manage.py migrate

echo "Starting gunicorn"
gunicorn --chdir=/app/tecgen \
    --workers=4 \
    --threads=6 \
    --worker-class=gthread \
    --preload \
    --bind :8000 \
    --log-level=info \
    --error-logfile - \
    --access-logfile - \
    --capture-output \
    shob.wsgi:application

cd -