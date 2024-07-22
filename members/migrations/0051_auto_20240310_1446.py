# Generated by Django 3.0.3 on 2024-03-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0050_event_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='hinweis',
            new_name='notes',
        ),
        migrations.AddField(
            model_name='event',
            name='public_event',
            field=models.BooleanField(default=False, verbose_name='Öffentliche Veranstaltung'),
        ),
        migrations.AlterField(
            model_name='event',
            name='info_only',
            field=models.BooleanField(default=True, verbose_name='Nur Ankündigung?'),
        ),
    ]