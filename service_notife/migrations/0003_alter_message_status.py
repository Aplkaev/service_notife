# Generated by Django 4.0.4 on 2022-05-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_notife', '0002_alter_mailing_options_message_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.IntegerField(),
        ),
    ]
