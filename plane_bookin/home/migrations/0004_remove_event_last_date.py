# Generated by Django 2.1.5 on 2019-03-01 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190301_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='last_date',
        ),
    ]
