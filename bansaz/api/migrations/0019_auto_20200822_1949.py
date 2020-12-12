# Generated by Django 3.0.8 on 2020-08-22 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200822_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_token_secret',
            field=models.CharField(default='HmOWiC4gSU8vh5J4puG2JTn3hCdKyKMgoIJhZfKH', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='refresh_token_secret',
            field=models.CharField(default='8KsEeLebMll3PqL4NsYcjAIv7ZUhKwbYAst8JDGo', max_length=50),
        ),
        migrations.CreateModel(
            name='RelationCalc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_relationcalc', to='api.Relation')),
                ('result_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_relationcalc', to='api.Relation')),
                ('second_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_relationcalc', to='api.Relation')),
            ],
        ),
    ]