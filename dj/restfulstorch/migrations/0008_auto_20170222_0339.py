# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restfulstorch', '0007_store_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesshours',
            name='weekday',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], verbose_name='weekday'),
        ),
        migrations.AlterField(
            model_name='store',
            name='details',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details_of', to='restfulstorch.StoreDetails', verbose_name='details of'),
        ),
    ]
