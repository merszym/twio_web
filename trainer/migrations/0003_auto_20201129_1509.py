# Generated by Django 3.0.3 on 2020-11-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0020_auto_20201127_0107'),
        ('trainer', '0002_table_entry_trainer_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table_entry',
            name='session',
            field=models.ManyToManyField(blank=True, null=True, to='members.Session'),
        ),
    ]