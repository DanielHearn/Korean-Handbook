# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-11 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180227_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crawl',
            old_name='Crawl_Name',
            new_name='crawl_name',
        ),
        migrations.RenameField(
            model_name='crawl',
            old_name='startdate',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='pub',
            old_name='Places_ID',
            new_name='places_id',
        ),
        migrations.RenameField(
            model_name='pub',
            old_name='Pub_Name',
            new_name='pub_name',
        ),
    ]