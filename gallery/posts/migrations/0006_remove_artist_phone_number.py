# Generated by Django 5.1.2 on 2024-10-18 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_artist_status_delete_artistregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='phone_number',
        ),
    ]