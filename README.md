# MyStartupManager

Welcome to **MyStartupManager**, an open source web application to manage
easily some parts of your startup company such as: leaves, employees,
contracts...

## How to contribute ?

These instructions are for Ubuntu LTS based distributions.

### Install Python

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

### Install project dependencies

Open a terminal:

```shell
$ mkvirtualenv -p /usr/bin/python3 -r requirements.txt mystartupmanager
```
