# Generated by Django 3.0.3 on 2022-06-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interested', '0015_auto_20220618_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicevent',
            name='thumbnail_high',
            field=models.ImageField(blank=True, null=True, upload_to='PublicEvents/Images/Headers', verbose_name='Thumbnail Portrait format'),
        ),
        migrations.AlterField(
            model_name='publicevent',
            name='thumbnail_long',
            field=models.ImageField(blank=True, null=True, upload_to='PublicEvents/Images/Headers', verbose_name='Thumbnail Landscape format'),
        ),
    ]
