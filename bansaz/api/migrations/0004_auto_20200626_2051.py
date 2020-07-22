# Generated by Django 3.0.7 on 2020-06-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200625_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='account_activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='token_code',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='token_expiration',
            field=models.DateTimeField(null=True),
        ),
    ]
