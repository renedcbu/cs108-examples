# Generated by Django 3.0.4 on 2020-04-03 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusmessage',
            name='timestamp',
        ),
    ]
