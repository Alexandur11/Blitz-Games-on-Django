# Generated by Django 5.1.4 on 2024-12-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blitz_games_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MusicPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
