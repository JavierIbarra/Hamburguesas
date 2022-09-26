# Hamburguesas

## Setup for testing purposes

1. Use **virtualenv** to create a virtual environment named **venv**
       virtualenv -p python3.10 venv

2. Activate the virtual environment

    Windows:
          
       .\venv\Scripts\activate
          
    Linux:
    
       source/bin/activate

3. Install all requirements listed in the **requirements.txt** file
          
       pip install -r requirements.txt

4. Create an **.env** file to store the following environment variables

       SECRET_KEY=<django_secret_key>
       DEBUG=True
       ALLOWED_HOSTS=*
       DATABASE_URL=<postgresql://USER_DB:PASSWORD_DB@DB_HOST:DB_PORT/DB_NAME>
       WEB_PORT=<HOST:PORT>
       DATABASE_NAME=<postgres_database_name>
       POSTGRES_USER=<postgres_user>
       POSTGRES_PASS=<postgres_password>

5. Migrations

        python manage.py makemigrations EP_Tutor
        python manage.py migrate 

6. Run the app
     
        python manage.py runserver