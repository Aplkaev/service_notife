# Generated by Django 4.0.4 on 2022-05-31 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_notife', '0005_mailing_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='end_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
