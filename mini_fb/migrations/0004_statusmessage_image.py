# Generated by Django 3.0.4 on 2020-04-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0003_statusmessage_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmessage',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
