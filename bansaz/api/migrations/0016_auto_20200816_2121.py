# Generated by Django 3.0.8 on 2020-08-16 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20200816_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_token_secret',
            field=models.CharField(default='0cWrX64HTG8qBXJq5bJEPIeMUnWalrvd8o91OVkp', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='refresh_token_secret',
            field=models.CharField(default='aDxXlurBtx85eI4Z84pDrh1Euj5OfEQ457tNqrmn', max_length=50),
        ),
    ]
