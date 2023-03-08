# Generated by Django 3.0.3 on 2023-03-08 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0041_message_autodelete'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payed', models.BooleanField(default=False, verbose_name='Bezahlt')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notizen')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Event')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('file', models.FileField(blank=True, null=True, upload_to='Events/Docs/etc/', verbose_name='File')),
                ('event_orga', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orga_docs', to='members.Event', verbose_name='Dokumente (Orga)')),
                ('event_public', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='public_docs', to='members.Event', verbose_name='Zusätzliche Dateien')),
                ('member_participants', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.MemberParticipant')),
            ],
        ),
    ]
