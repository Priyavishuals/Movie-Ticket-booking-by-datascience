# Generated by Django 2.1.5 on 2019-03-02 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190302_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='each_entry_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]