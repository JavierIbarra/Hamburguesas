#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

#echo "Flusing django manage command"
#python manage.py flush --no-input

python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
python manage.py runserver $WEB_HOST:$WEB_PORT