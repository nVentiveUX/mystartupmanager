# Developer Guide

This guide will help those who want to participate to the project giving them
some advices for setting up their development environment.

Most of the instructions here are tested for Ubuntu LTS / Archlinux based
workstations.

## Install Python environment

Install **Python 3**:

```shell
# Ubuntu
sudo apt-get install python3-dev python3-pip

# Archlinux
sudo pacman -S python python-pip
```

Install **virtualenvwrapper**:

```shell
sudo pip install virtualenvwrapper
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
```

Your development environment is now ready.
Enable virtual environment prior to any commands from now:

```shell
workon mystartupmanager
```

## Database backend

Here are some instructions on the supported database backend used in
development.

### SQLite

SQLite is the default database backend, you have nothing more to do in order
to make use of it.

### PostgresSQL

Start a [PostgresSQL 9.4](https://hub.docker.com/_/postgres/) container using
[docker](https://www.docker.com/):

```shell
docker run \
    --name mystartupmanager_db \
    -p 127.0.0.1:9000:5432 -e POSTGRES_PASSWORD=dbpwd -d postgres:9.4
```

The database server is accessible using `psql` utility with **postgres** user
and **dbpwd** for its password:

```shell
psql -h localhost -p 9000 -U postgres
```

Create development database:

```shell
createdb -h localhost -p 9000 -U postgres -E UTF8 -e mystartupmanager_dev
```

If you need to delete the database and create it again, drop it before:

```shell
dropdb -h localhost -p 9000 -U postgres -e mystartupmanager_dev
```

## Install project dependencies

Across the whole documentation we will make use of **mystartupmanager** Python
virtual environment. Here are the instructions to setup it:

```shell
mkvirtualenv -p /usr/bin/python3 -r requirements/develop.txt mystartupmanager
```

Activate the virtual environment with:

```shell
workon mystartupmanager
```

We assume that starting from here, the virtual environment is enabled wih the
previous command.

Time to time, you will need to update the dependencies, do it with:

```shell
pip install --upgrade -r requirements/develop.txt
```

## Populate database

Initialize the database schema:

```shell
# Run database migrations
./manage.py migrate
```

Create an **admin** account:

```shell
# Create administrator account and set password
./manage.py createsuperuser --username admin --email admin@localhost --noinput
./manage.py changepassword admin
```

## Test

Run the test server with:

```shell
# Run the test server
./manage.py runserver
```
