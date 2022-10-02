FROM python:3.10.6

ARG WEB_PORT

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

#CMD python manage.py runserver ${WEB_PORT}
ENTRYPOINT [ "./docker/docker-entrypoint.sh" ]