# Copyright (c) 2016 nVentiveUX
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Setuptools packaging"""

from setuptools import setup, find_packages


# Read requirements
try:
    with open('requirements/base.txt', encoding='utf-8') as requirements:
        requires_list = requirements.readlines()
except IOError as e:
    print('Error: can\'t read requirements file: ', e)
    raise SystemExit(1)

# Setuptools main
setup(
    name='mystartupmanager',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/nVentiveUX/mystartupmanager',
    license='MIT',
    author='nVentiveUX',
    # TODO: we need a team email here ! ;-)
    author_email='besancon.vincent@gmail.com',
    description='A Django project to help new entrepreneurs',
    install_requires=requires_list,
)
