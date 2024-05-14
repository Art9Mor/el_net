# Electronic store ElNet  

Online platform for electronics retail chain

## Description

Here is an API service for a network selling electronics.  
This project provides an opportunity to get acquainted with various types of electrical appliances and sellers right up to the manufacturing plant.

## Instructions  

1. Clone the repository  

   - https

          git clone https://github.com/Art9Mor/el_net.git

   - ssh

          git clone git@github.com:Art9Mor/el_net.git

2. Set up environment variables

    - Create an `.env` file in the project root
    - Copy the contents from `.env.sample` to the file you created
    - Fill in the variable values with your data
   
   Variable values:

        
        DJANGO_SECRET_KEY=write_your_secret_key_for_django_project

        DEBUG=debug_mode (must be in "False" mode if used in a production environment)
        DJANGO_ALLOWED_HOSTS=write_here_hosts_to_allow_them
        
        # for runserver
        POSTGRES_DB=your_database_name
        POSTGRES_USER=your_database_user
        POSTGRES_PASSWORD=your_database_password
        
        # for docker compose
        HOST=your_host_name
        PORT=your_release_port
        
        LANGUAGE_CODE=chose_your_language
        TIME_ZONE=your_timezone

        # for admin user creation
        ADMIN_EMAIL=
        ADMIN_FIRST_NAME=
        ADMIN_LAST_NAME=
        ADMIN_ROLE=
        ADMIN_PASSWORD=
        

3. Installing Requirements and Migrations

There are two ways to do this: manually and using a special script

- Using a script:

There is a script `deploy.sh` in the root folder of the project.
The `deploy.sh` script runs a series of commands to prepare and deploy a Django application.

`python3 -m venv env`: Creates a virtual Python environment called `env` that isolates your project's dependencies from the global system.

`source env/bin/activate`: Activates the virtual environment.

`pip3 install -r requirements.txt`: Installs all required dependencies for the project, listed in the `requirements.txt` file.

`python3 manage.py create_db`: Creates (and updates if available) a new database on your local server.

`python3 manage.py migrate`: Applies all database migrations.

`python3 manage.py collectstatic --no-input`: Collects static application files into one directory.

`deactivate`: Deactivates the virtual environment, returning you to the global environment.


- Manual:

Write the commands from `deploy.sh` manually on the command line of your IDE.
In this case the `python3 manage.py create_db` command is optional.


4. Starting the server

There are several options for how you can run the server: locally or using docker
- locally:

        python3 manage.py runserver

- using docker:

        docker build -t app-name .

        docker run -p 8000:8000 app-name

- docker compose:

        docker compose up --build

## Some helpful commands

1. Admin

        python3 manage.py create_admin

This command creates a user with administrator rights.
This user has some fields:

        email
        first_name
        last_name
        role
        password


You can fill them in the `.env` file.

2. Simple user

        python3 manage.py create_user

This command creates an authenticated user with fields

        email='simpleuser@elnet.com',
        first_name='John',
        last_name='Doe',
        role='user',
        password='simpleuserpassword'


## Main stack

- python(3.11)
- Django(5.0.5)
- django-dotenv(1.4.2)
- django-filter(24.2)
- django-restframework(0.0.1)
- djangorestframework-simplejwt(5.3.1)
- djoser(2.2.2)
- drf-yasg(1.21.7)
- psycopg2-binary(2.9.9)