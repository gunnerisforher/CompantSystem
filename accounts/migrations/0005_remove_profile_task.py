# Generated by Django 4.1.2 on 2022-11-02 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='task',
        ),
    ]
