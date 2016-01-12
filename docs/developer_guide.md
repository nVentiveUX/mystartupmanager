# Developer Guide

This guide will help those who want to participate to the project giving them
some advices for setting up their development environment.

Most of the instructions here are tested for Ubuntu LTS / Archlinux based
workstations.

## Install Python environment

Install **Python 3**:

```shell
# Ubuntu
$ sudo apt-get install python3-dev python3-pip

# Archlinux
$ sudo pacman -S python python-pip
```

Install **virtualenvwrapper**:

```shell
$ sudo pip install virtualenvwrapper
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
```

Your development environment is now ready.
Enable virtual environment prior to any commands from now:

```shell
$ workon mystartupmanager
```

## Test database instance

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
