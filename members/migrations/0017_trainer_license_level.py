# Generated by Django 3.0.3 on 2020-11-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_auto_20201126_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='license_level',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Lizenzstufe'),
        ),
    ]
