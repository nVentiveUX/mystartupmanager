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

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from core.models import AbstractPhoneNumber


class Employee(models.Model):
    """
    An employee in the company.

    This class extends the User model with extra fields for employee details.
    """
    GENDER_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
    )

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name=_('profile'))
    gender = models.CharField(_('gender'),
                              max_length=1,
                              choices=GENDER_CHOICES,
                              blank=True,
                              null=True)
    job_title = models.CharField(_('job title'),
                                 max_length=255,
                                 default='')

    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')

    def __str__(self):
        return '{fullname}'.format(fullname=self.user.get_full_name())


class PhoneNumber(AbstractPhoneNumber):
    """Store a labilized phone number in a user profile."""
    employee = models.ForeignKey(Employee,
                                 on_delete=models.CASCADE,
                                 related_name='phones')


# Define a signal to create the employee profile for new users.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_employee_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        employee_profile = Employee(user=instance)
        employee_profile.save()
