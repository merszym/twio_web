# Generated by Django 3.2.8 on 2024-04-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0076_auto_20240407_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]