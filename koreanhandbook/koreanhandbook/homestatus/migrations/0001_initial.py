# Generated by Django 2.0.4 on 2018-10-09 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_value', models.IntegerField(default='0')),
                ('date_inserted', models.DateTimeField(default=datetime.datetime(2018, 10, 9, 11, 39, 45, 114257))),
            ],
        ),
    ]
