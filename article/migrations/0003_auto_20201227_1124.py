# Generated by Django 3.1.2 on 2020-12-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20201227_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='snippet',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]