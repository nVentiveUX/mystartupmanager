# MyStartupManager

Welcome to **MyStartupManager**, an open source web application to manage
easily some parts of your startup company such as: leaves, employees,
contracts...

# How to contribute ?

These instructions are for Ubuntu LTS based distributions.

## Install Python

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

## Project configuration

### Install project dependencies

Open a terminal:

```shell
$ mkvirtualenv -p /usr/bin/python3 -r requirements.txt mystartupmanager
```

### Run database migrations

```shell
$ ./manage.py migrate
```

### Create administration account

```shell
$ ./manage.py createsuperuser --username admin --email admin@localhost --noinput
$ ./manage.py changepassword admin
<enter password>
```

### Run the test server

```shell
$ ./manage.py runserver
$ xdg-open http://127.0.0.1:8000/
```

**Site administration** is accessible from relative path `/admin`. Login using
the administration account created earlier.
