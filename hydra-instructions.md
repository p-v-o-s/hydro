## if you don't have ca-certificates for curl, first:

sudo apt-get install ca-certificates

sudo mkdir -p /etc/pki/tls/certs
sudo cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt
curl -fsSL https://get.docker.com/ | sh

as prompted, run:
sudo usermod -aG docker dwblair

log out, log back in 

## installation

sudo pip install docker-compose
docker-compose -f dev.yml  up -d

## test / check

> run: 

docker ps 

> or alternatively command:

docker-compose -f dev.yml ps 

note: in dev.yml, 

django:
  dockerfile: Dockerfile-dev
  build: .
  command: python /app/manage.py runserver_plus 0.0.0.0:8000
  volumes:
    - .:/app
  ports:
    - "8000:8000"
  links:
    - postgres
    
note: the '8000' in the "command:" section needs to be consistent with the second '8000' in the 'ports:' section 

the first '8000' in the 'ports:' section refers to the host port which you should access locally, by using 'localhost:8000' in the browser.


## create database

while the container is running, need to create the database ...

docker-compose -f dev.yml run django python manage.py migrate 

## to create a superuser/admin for the site

docker-compose -f dev.yml run django python manage.py createsuperuser


## unit tests

docker-compose -f dev.yml run django python manage.py test device

## changing the backend

inside config/settings ...

common.py  __init__.py  local.py  production.p

local.py 



## hdf5 (maybe)

https://pypi.python.org/pypi/hdf5-django/0.1.2


