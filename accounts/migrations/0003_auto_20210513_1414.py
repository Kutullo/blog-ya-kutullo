# Generated by Django 3.1.2 on 2021-05-13 12:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_userprofiles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfiles',
            new_name='UserProfile',
        ),
    ]