# MyStartupManager

[![Build Status](https://travis-ci.org/nVentiveUX/mystartupmanager.svg)](https://travis-ci.org/nVentiveUX/mystartupmanager)

Welcome to **MyStartupManager**, an open source web application to manage
easily some parts of your startup company such as: leaves, employees,
contracts...

## Contents

* [How to contribute ?](https://github.com/nVentiveUX/mystartupmanager/wiki/How-to-contribute)
* [Licensing](https://github.com/nVentiveUX/mystartupmanager/blob/master/LICENSE)

## Quick start

```shell
# Install project dependencies
mkvirtualenv -p /usr/bin/python3 -r requirements/develop.txt mystartupmanager

# Run database migrations
./manage.py migrate

# Create administrator account and set password
./manage.py createsuperuser --username admin --email admin@localhost --noinput
./manage.py changepassword admin

# Run the test server
./manage.py runserver
```

Test server is listening on http://127.0.0.1:8000.

**Site administration** is accessible from http://127.0.0.1:8000/admin. Login using
the administration account created earlier.

**[Back to top](#contents)**
