# Generated by Django 3.1.2 on 2021-01-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0018_auto_20210116_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='reading_min',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
