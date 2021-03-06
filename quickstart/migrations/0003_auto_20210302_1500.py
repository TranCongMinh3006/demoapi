# Generated by Django 3.1.2 on 2021-03-02 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0002_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Categorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Article_Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.TextField()),
                ('representation', models.TextField()),
                ('displayContent', models.TextField()),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('click_counter', models.IntegerField()),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('articleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.articles')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User_Views',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_view', models.DateTimeField(auto_now_add=True)),
                ('articleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.articles')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='article_tags',
            name='articleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.articles'),
        ),
        migrations.AddField(
            model_name='article_tags',
            name='tagID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.tags'),
        ),
        migrations.AddField(
            model_name='article_categorys',
            name='articleID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.articles'),
        ),
        migrations.AddField(
            model_name='article_categorys',
            name='categoryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.categorys'),
        ),
    ]
