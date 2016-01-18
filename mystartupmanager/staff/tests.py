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

"""Module testing"""

from django.test import TestCase
from django.contrib.auth.models import User

from mystartupmanager.staff.models import Employee


class EmployeeTestCase(TestCase):
    def setUp(self):
        new_user = User.objects.create(username='foo',
                                       first_name='Foo',
                                       last_name='BAR',
                                       email='foo.bar@localhost',
                                       password='foobar')
        new_user.profile.gender = 'M'
        new_user.profile.job_title = 'Tester'
        new_user.profile.phones.create(label='Home',
                                       number='+33111111111')
        new_user.profile.save()

    def test_employee_profile_exist(self):
        """Test that newly created users have an employee profile."""
        foobar_employee = User.objects.get(username='foo')
        self.assertEqual(foobar_employee.profile.job_title, 'Tester')
