# Generated by Django 3.0.8 on 2020-07-23 13:11

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200723_0452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='colleges',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='degrees',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='education_status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='emails',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='myarr',
            field=api.models.MyArrayField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_numbers',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='relationship_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='schools',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='workplace',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='access_token_secret',
            field=models.CharField(default='x83wxoeZ2uynRBCXcouQbs3OyyFeeIYPD5cun7lB', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='refresh_token_secret',
            field=models.CharField(default='ORF7IJO4XO7J6rk6Z6m0C4ieSp1FzhWKaBQiQSzi', max_length=50),
        ),
    ]
