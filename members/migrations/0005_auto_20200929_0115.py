# Generated by Django 3.0.3 on 2020-09-28 23:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20200927_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description_rendered',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 1, 15, 51, 743424), verbose_name='Anmeldung/Abmeldung bis'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 1, 15, 51, 743474), verbose_name='Datum Ende'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 1, 15, 51, 743455), verbose_name='Datum Beginn'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 1, 15, 51, 747285)),
        ),
    ]