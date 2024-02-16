# Generated by Django 2.1.5 on 2019-03-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190302_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='From',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='booking',
            name='To',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_preference',
            field=models.CharField(choices=[('Moring 9-12', ' Moring 9-12 '), ('12-3 ', '12-3'), ('3-6', '3-6'), ('6-9', '6-9'), ('night 9-12', 'night 9-12')], default=0, max_length=10),
        ),
    ]