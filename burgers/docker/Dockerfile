FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

RUN chmod +x ./docker/docker-entrypoint.sh

ENTRYPOINT [ "./docker/docker-entrypoint.sh" ]