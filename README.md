# TEST TASK FROM Rulebreakers

# TO RUN CODE YOU SHOULD FOLLOW NEXT STEPS

1. pull this repo
2. create .env file in project directory with following variables:
    - SECRET_KEY
    - DEBUG 
    - DJANGO_ALLOWED_HOSTS 
    - POSTGRES_USER
    - POSTGRES_PASSWORD
    - POSTGRES_DB
    - POSTGRES_HOST
    - POSTGRES_PORT
3. if you have docker:
   - you should build docker image with name testtask:latest or whatever you want but don't forget
   change the image name in docker-compose file
   - build image with command docker build -t testtask:latest .
   - docker compose up to run 
4. if you don't have docker:
   - run app with following steps:
     - pip3 install -r requirements.txt
     - python3 manage.py makemigrations
     - python3 manage.py migrate
     - python3 manage.py runserver

5. You can access swagger docs in: http://localhost:8000/swagger/ or  http://0.0.0.0:8000/swagger/
6. And you can also access django admin panel on default admin link page /admin, but first you should create user to access it.

PS: don't forget collect static files(python3 manage.py collectstatic)
