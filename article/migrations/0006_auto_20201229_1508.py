# Generated by Django 3.1.2 on 2020-12-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20201227_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
