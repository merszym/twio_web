# Generated by Django 3.0.3 on 2024-03-11 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0056_auto_20240310_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='shopitem',
            name='gallery',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='ShopItem',
        ),
    ]