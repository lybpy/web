# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-16 14:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180116_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='catgory',
            new_name='category',
        ),
    ]
