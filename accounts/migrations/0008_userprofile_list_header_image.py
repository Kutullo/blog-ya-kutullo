# Generated by Django 3.1.2 on 2021-05-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210526_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='list_header_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
