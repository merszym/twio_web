# Generated by Django 3.0.3 on 2024-03-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0068_auto_20240323_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='short',
            field=models.TextField(blank=True, null=True, verbose_name='Kurzbeschreibung'),
        ),
    ]