# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restfulstorch', '0016_auto_20170129_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateField()),
                ('store_code', models.BigIntegerField(unique=True)),
                ('store_name', models.CharField(max_length=48)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=8)),
                ('address', models.TextField()),
                ('primary_phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('secondary_phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('website_address', models.CharField(blank=True, max_length=128, null=True)),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_phone_number', models.CharField(max_length=11)),
                ('contact_email_address', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], unique=True)),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restfulstorch.Company')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='sellers',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
        migrations.AddField(
            model_name='category',
            name='companies',
            field=models.ManyToManyField(blank=True, to='restfulstorch.Company'),
        ),
    ]