FROM python:3.8-slim-buster

WORKDIR /python-docker
EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x ./docker/docker-entrypoint.sh

ENTRYPOINT [ "./docker/docker-entrypoint.sh" ]