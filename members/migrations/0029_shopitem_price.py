# Generated by Django 3.0.3 on 2022-03-15 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0028_auto_20220315_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitem',
            name='price',
            field=models.IntegerField(blank=True, default=10, verbose_name='Price'),
            preserve_default=False,
        ),
    ]