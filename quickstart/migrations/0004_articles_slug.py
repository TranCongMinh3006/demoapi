# Generated by Django 3.1.2 on 2021-03-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20210302_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default='slug', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]