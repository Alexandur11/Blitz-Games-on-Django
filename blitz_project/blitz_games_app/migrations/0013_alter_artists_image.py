# Generated by Django 5.1.4 on 2024-12-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blitz_games_app', '0012_alter_artists_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='image',
            field=models.URLField(default='https://www.pexels.com/photo/man-standing-in-front-of-microphone-4073982/'),
        ),
    ]