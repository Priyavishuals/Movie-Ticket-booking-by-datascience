# Generated by Django 2.1.5 on 2019-03-02 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_event_last_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='last_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
