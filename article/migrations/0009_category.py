# Generated by Django 3.1.2 on 2020-12-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_article_article_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
