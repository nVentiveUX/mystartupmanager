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

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mystartupmanager.staff.models import Employee, PhoneNumber


class EmployeePhoneNumbersInline(admin.StackedInline):
    model = PhoneNumber
    extra = 0


@admin.register(Employee)
class EmployeeProfileAdmin(admin.ModelAdmin):
    inlines = (EmployeePhoneNumbersInline,)
    list_display = ('full_name', 'username', 'gender', 'list_phones')
    readonly_fields = ('user',)

    def username(self, obj):
        return obj.user.username
    username.short_description = _('username')

    def full_name(self, obj):
        return obj.user.get_full_name()
    full_name.short_description = _('full name')

    def list_phones(self, obj):
        phones = ['%s' % p for p in obj.phones.all()]
        return ', '.join(phones)
    list_phones.short_description = _('phone numbers')

    def has_add_permission(self, request, obj=None):
        # Employee profiles are added when new users are created.
        return False

    def has_delete_permission(self, request, obj=None):
        # Employee profile are deleted when the associated user is deleted.
        return False
