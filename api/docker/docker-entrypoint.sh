#!/bin/bash

# Start server
echo "Starting server"
python manage.py runserver $WEB_HOST:$WEB_PORT