# Generated by Django 3.0.8 on 2020-07-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200723_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_token_secret',
            field=models.CharField(default='Csi94sYy9htnQe5PpHdNm12KZHdB11q1dwuaMPok', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='refresh_token_secret',
            field=models.CharField(default='RnFTxZsUmsyhtZE4Ur8li2gdYgv6NoRb5ndUyT9R', max_length=50),
        ),
    ]
