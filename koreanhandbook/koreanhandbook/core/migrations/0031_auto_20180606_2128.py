# Generated by Django 2.0.4 on 2018-06-06 20:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20180604_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(default='Stage Name', max_length=100)),
                ('birth_name', models.CharField(default='Birth Name', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_1', models.CharField(max_length=255)),
                ('col_2', models.CharField(max_length=255)),
                ('date_inserted', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('member', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Full Name', max_length=100)),
                ('short_name', models.CharField(default='shortname', max_length=100)),
                ('korean_name', models.CharField(default='한국어', max_length=100)),
                ('picture', models.ImageField(upload_to='')),
                ('home_focus', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='info',
            name='description',
            field=models.TextField(default='The Korean names for the _ with their English translations.'),
        ),
        migrations.AlterField(
            model_name='row_2',
            name='info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Info'),
        ),
        migrations.AlterField(
            model_name='row_3',
            name='info',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Info'),
        ),
        migrations.AddField(
            model_name='member',
            name='profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
    ]
