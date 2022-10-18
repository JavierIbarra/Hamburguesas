# Hamburguesas

## Running using local kubernetes

       kind create cluster
       sh kubernetes/kubernetes.sh

## Running using docker

1. Create the **.env** files where the **env.example** files with the corresponding format exist

    burger/docker/.env
              SECRET_KEY=<django_secret_key>
              DEBUG=True
              ALLOWED_HOSTS=*
              DATABASE_URL=<postgresql://USER_DB:PASSWORD_DB@DB_HOST:DB_PORT/DB_NAME>
              WEB_HOST=<host>
              DATABASE_NAME=<postgres_database_name>
              POSTGRES_USER=<postgres_user>
              POSTGRES_PASS=<postgres_password>
       
    postgres/docker/.env
              POSTGRES_DB=<postgres_database_name>
              POSTGRES_USER=<postgres_user>
              POSTGRES_PASSWORD=<postgres_password>
              PGDATA=/var/lib/postgresql/data/pgdata
              
    odoo/docker/.env
              HOST=<host>
              PORT=5432
              USER=<postgres_user>
              PASSWORD=<postgres_password>

2. Run docker compose

       docker-compose -f docker-compose-old.yml up --build

## Setup for testing purposes

1. Start a PostgreSQL server

       docker run -d -e POSTGRES_USER=<postgres_user> -e POSTGRES_PASSWORD=<postgres_password> -e POSTGRES_DB=<postgres_database_name> --name db -p 5432:5432 postgres:latest
       
2. Use **virtualenv** to create a virtual environment named **venv**

       virtualenv -p python3.10 venv
       
3. Activate the virtual environment

    Windows:
          
       .\venv\Scripts\activate
          
    Linux:
    
       source /bin/activate

4. Install all requirements listed in the **requirements.txt** file
          
       pip install -r requirements.txt

5. Create an **.env** file to store the following environment variables

       burger/docker/.env
              SECRET_KEY=<django_secret_key>
              DEBUG=True
              ALLOWED_HOSTS=*
              DATABASE_URL=<postgresql://USER_DB:PASSWORD_DB@DB_HOST:DB_PORT/DB_NAME>
              WEB_HOST=<host>
              DATABASE_NAME=<postgres_database_name>
              POSTGRES_USER=<postgres_user>
              POSTGRES_PASS=<postgres_password>
       
       postgres/docker/.env
              POSTGRES_DB=<postgres_database_name>
              POSTGRES_USER=<postgres_user>
              POSTGRES_PASSWORD=<postgres_password>
              PGDATA=/var/lib/postgresql/data/pgdata
              
       odoo/docker/.env
              HOST=<host>
              PORT=5432
              USER=<postgres_user>
              PASSWORD=<postgres_password>

6. Migrations

        python manage.py migrate 

7. Run the app
     
        python manage.py runserver
