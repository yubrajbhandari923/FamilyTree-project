# Generated by Django 3.0.7 on 2020-06-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200626_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='token_code',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='token_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
