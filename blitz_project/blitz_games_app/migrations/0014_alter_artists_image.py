# Generated by Django 5.1.4 on 2024-12-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blitz_games_app', '0013_alter_artists_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='image',
            field=models.URLField(default='https://img.freepik.com/premium-vector/man-singer-silhouette-man-singing-mic-singer-singing-silhouette-vocalist-singing-microphone_690577-1487.jpg?w=1060'),
        ),
    ]