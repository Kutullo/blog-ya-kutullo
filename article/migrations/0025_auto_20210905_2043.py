# Generated by Django 3.1.2 on 2021-09-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0024_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='snippet',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
