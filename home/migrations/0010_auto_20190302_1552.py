# Generated by Django 2.1.5 on 2019-03-02 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_booking_each_entry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='event_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_preference',
            field=models.CharField(choices=[('9-12', '9-12'), ('12-3', '12-3'), ('3-6', '6-9'), ('6-9', '6-9'), ('9-12', '9-12')], default=0, max_length=10),
        ),
    ]
