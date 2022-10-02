#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput


# Start server
echo "Starting server"
python manage.py runserver $WEB_HOST:$WEB_PORT