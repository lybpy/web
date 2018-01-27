# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-17 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20180117_1228'),
        ('courses', '0002_auto_20180113_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg'),
        ),
    ]
