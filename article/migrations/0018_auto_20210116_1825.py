# Generated by Django 3.1.2 on 2021-01-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20210111_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
