# Generated by Django 3.0.3 on 2021-05-10 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interested', '0007_auto_20210510_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventparticipant',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notizen'),
        ),
    ]