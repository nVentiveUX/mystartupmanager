# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 01:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='gender')),
                ('job_title', models.CharField(default='', max_length=255, verbose_name='job title')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=32, verbose_name='phone_label_field')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='phone_number_field')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='staff.Employee')),
            ],
            options={
                'verbose_name': 'phone number',
                'abstract': False,
                'verbose_name_plural': 'phone numbers',
            },
        ),
    ]
