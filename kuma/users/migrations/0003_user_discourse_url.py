# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 15:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_pytz_2018_5_and_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='discourse_url',
            field=models.TextField(blank=True, validators=[django.core.validators.RegexValidator(b'^https://discourse\\.mozilla\\.org/u/', 'Enter a valid Discourse URL.', b'invalid')], verbose_name='Discourse'),
        ),
    ]
