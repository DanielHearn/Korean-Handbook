# Generated by Django 2.0.4 on 2018-06-07 16:53

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20180606_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member_info',
            name='member',
        ),
        migrations.AddField(
            model_name='member',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(default='default.jpg', upload_to='./static/media/images'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=imagekit.models.fields.ProcessedImageField(default='default.jpg', upload_to='./static/media/images'),
        ),
        migrations.DeleteModel(
            name='Member_Info',
        ),
    ]