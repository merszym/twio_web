# Generated by Django 3.0.3 on 2024-07-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0077_alter_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='external_spots',
            field=models.IntegerField(blank=True, null=True, verbose_name='Anzahl Plätze für Nichtmitglieder'),
        ),
        migrations.AddField(
            model_name='event',
            name='header',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/events/img/', verbose_name='Header'),
        ),
        migrations.AddField(
            model_name='event',
            name='square',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/events/img/', verbose_name='Thumbnail'),
        ),
    ]
