# Generated by Django 2.0.2 on 2022-05-26 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField(unique=True)),
                ('phone', models.IntegerField(max_length=11)),
                ('code', models.IntegerField(max_length=3)),
                ('tag', models.TextField(verbose_name='Тэг')),
                ('time_zone', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.IntegerField(unique=True)),
                ('start_time', models.DateTimeField()),
                ('message', models.TextField(verbose_name='Текст рассылки')),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(verbose_name=-1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service_notife.Client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service_notife.Mailing')),
            ],
        ),
    ]