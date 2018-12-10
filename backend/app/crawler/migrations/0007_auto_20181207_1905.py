# Generated by Django 2.1.2 on 2018-12-07 19:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0006_auto_20181207_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 19, 5, 15, 975326, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='node',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 19, 5, 15, 975400, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 19, 5, 15, 975326, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 19, 5, 15, 975400, tzinfo=utc)),
        ),
    ]
