# Generated by Django 2.0.4 on 2018-06-06 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20180606_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birth_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
