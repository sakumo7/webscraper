# Generated by Django 2.1.2 on 2018-12-06 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='crawler',
            field=models.CharField(choices=[('0', 'GenericCrawler')], default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='images_storage',
            field=models.CharField(choices=[('0', 'local'), ('1', 's3')], default='0', max_length=1),
        ),
    ]
