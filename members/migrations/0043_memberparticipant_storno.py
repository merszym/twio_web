# Generated by Django 3.0.3 on 2023-03-08 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0042_document_memberparticipant'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberparticipant',
            name='storno',
            field=models.BooleanField(default=False, verbose_name='Storno'),
        ),
    ]