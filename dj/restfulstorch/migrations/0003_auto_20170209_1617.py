# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restfulstorch', '0002_auto_20170209_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent',
            new_name='children',
        ),
    ]
